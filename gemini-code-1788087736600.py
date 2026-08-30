from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str) -> str:
    """Argon2 ile güvenli şifre hashleme."""
    return ph.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Argon2 şifre doğrulama."""
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False