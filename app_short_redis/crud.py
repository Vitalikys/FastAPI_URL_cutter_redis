import secrets
import string


def create_random_key(length: int = 5) -> str:
    """ create random secret key, will use for url link """
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

