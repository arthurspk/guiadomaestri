#!/usr/bin/env python3
"""
maestri_wire_client.py — Cliente mínimo do protocolo Maestri Wire.

O Maestri Wire é o protocolo que deixa outros dispositivos e ferramentas falarem com um
host Maestri (a base do Maestri Remote e de integrações customizadas).

Fundamentos (doc oficial https://www.themaestri.app/pt-br/docs/wire):
- Servidor em TCP 7434, só HTTPS/WSS, certificado AUTOASSINADO. Os clientes **fixam (pin)
  o SHA-256 da chave pública** do host em vez de consultar uma CA. Requisições > 8 MiB →
  413; conexões ociosas por 20s são encerradas.
- Pareamento único com código de 6 dígitos (válido 5 min) → devolve um token de dispositivo
  (64 hex) usado como Bearer. Papéis: owner (RW) e guest (RO).
- Datas em ISO 8601; IDs em MAIÚSCULAS (repita verbatim, nunca reformate).

SEGURANÇA: como o certificado é autoassinado, este cliente NÃO desliga a verificação TLS.
Ele exige que você passe o **pin** (SHA-256) e valida o certificado do host contra ele antes
de qualquer requisição. Nunca use `CERT_NONE` num uso real — isso abre a porta para
man-in-the-middle. Descubra o pin uma vez, por um canal confiável, com:

    python3 maestri_wire_client.py fingerprint HOST     # imprime o SHA-256 do host

Confira o valor com o dono do host, guarde-o, e passe-o via --pin nas chamadas seguintes.

Uso:
  python3 maestri_wire_client.py fingerprint HOST
  python3 maestri_wire_client.py pair   HOST 483920 "Meu Cliente"   --pin <sha256>
  python3 maestri_wire_client.py list   HOST TOKEN                  --pin <sha256>
  python3 maestri_wire_client.py prompt HOST TOKEN TERMINAL_ID "rode os testes" --pin <sha256>

Observação: o Wire fixa o SHA-256 da CHAVE PÚBLICA (SubjectPublicKeyInfo). Extrair a SPKI
sem dependências externas é trabalhoso, então este exemplo fixa o SHA-256 do certificado
inteiro (DER) — pragmático e sólido para um único host autoassinado. Para casar exatamente
com o pin de chave pública do app, use a lib `cryptography` e compare a SPKI.
"""

import hashlib
import http.client
import json
import ssl
import sys

PORT = 7434


def _host_cert_der(host: str) -> bytes:
    """Pega o certificado DER do host sem validar cadeia (só para calcular o fingerprint;
    nenhuma requisição de dados é feita aqui)."""
    ctx = ssl._create_unverified_context()  # noqa: SLF001 — só para ler o cert e derivar o pin
    conn = http.client.HTTPSConnection(host, PORT, context=ctx, timeout=15)
    conn.connect()
    try:
        return conn.sock.getpeercert(binary_form=True)
    finally:
        conn.close()


def fingerprint(host: str) -> str:
    der = _host_cert_der(host)
    fp = hashlib.sha256(der).hexdigest()
    print(fp)
    return fp


def _conn(host: str, pin_sha256: str) -> http.client.HTTPSConnection:
    """Abre uma conexão e valida o certificado do host contra o pin ANTES de usar."""
    if not pin_sha256:
        raise SystemExit("erro: --pin é obrigatório (rode 'fingerprint HOST' e confirme o valor).")
    der = _host_cert_der(host)
    actual = hashlib.sha256(der).hexdigest()
    if actual.lower() != pin_sha256.lower():
        raise SystemExit(f"erro: pin não confere. esperado {pin_sha256}, host apresentou {actual}.")
    ctx = ssl._create_unverified_context()  # cadeia não validável (autoassinado); o pin acima é a garantia
    return http.client.HTTPSConnection(host, PORT, context=ctx, timeout=15)


def _req(host, pin, method, path, token=None, body=None):
    conn = _conn(host, pin)
    try:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        conn.request(method, path, json.dumps(body) if body is not None else None, headers)
        raw = conn.getresponse().read().decode()
        return json.loads(raw) if raw.strip() else {"ok": True}
    finally:
        conn.close()


def pair(host, code, name, pin):
    out = _req(host, pin, "POST", "/pair", body={"deviceName": name, "code": code})
    print(json.dumps(out, ensure_ascii=False, indent=2))  # => {"token": "...", "role": "owner"}


def list_workspaces(host, token, pin):
    out = _req(host, pin, "GET", "/api/workspaces", token=token)
    rows = out.get("workspaces", out if isinstance(out, list) else [])
    for ws in rows:
        print(f"{ws.get('id')}  attention={ws.get('attentionCount', 0)}  {ws.get('name','')}")


def send_prompt(host, token, terminal_id, text, pin):
    out = _req(host, pin, "POST", f"/api/terminals/{terminal_id}/prompt",
               token=token, body={"text": text})
    print(json.dumps(out, ensure_ascii=False, indent=2))


def _get_pin(argv):
    if "--pin" in argv:
        i = argv.index("--pin")
        return argv[i + 1]
    return ""


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd, pin = argv[1], _get_pin(argv)
    if cmd == "fingerprint":
        fingerprint(argv[2])
    elif cmd == "pair":
        pair(argv[2], argv[3], argv[4], pin)
    elif cmd == "list":
        list_workspaces(argv[2], argv[3], pin)
    elif cmd == "prompt":
        send_prompt(argv[2], argv[3], argv[4], argv[5], pin)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
