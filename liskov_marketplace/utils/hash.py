import hashlib


def sha256(value: str) -> bytes:
    m = hashlib.sha256()
    m.update(value.encode("utf-8"))
    return m.digest()
