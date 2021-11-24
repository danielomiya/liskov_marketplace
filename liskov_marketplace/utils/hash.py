import hashlib


def sha256(value: str) -> bytes:
    """
    Hashes a string using the SHA256 algorithm

    Args:
        value (str): value to be hashed

    Returns:
        bytes: bytes of the hashed string
    """
    m = hashlib.sha256()
    m.update(value.encode("utf-8"))
    return m.digest()
