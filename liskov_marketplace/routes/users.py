from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, request

from liskov_marketplace.models.user import User
from liskov_marketplace.repositories.base_repository import BaseRepository
from liskov_marketplace.repositories.in_memory_repository import InMemoryRepository
from liskov_marketplace.typing import Response
from liskov_marketplace.utils.functions import identity
from liskov_marketplace.utils.hash import sha256
from liskov_marketplace.utils.http_error import create_error

bp = Blueprint("users", __name__)
users_repository: BaseRepository[User] = InMemoryRepository()


@bp.post("/api/users")
def create_user() -> Response:
    """
    Creates an user

    Returns:
        Response: the user itself in case of success or error
    """
    body = request.get_json() or {}
    keys = {
        "name": identity,
        "birth_date": lambda d: datetime.strptime(d, "%Y-%m-%d"),
        "cpf_cnpj": identity,
        "email": str.lower,
        "phone": identity,
        "password": sha256,
    }

    if any(key not in body for key in keys):
        return create_error(
            f"not all required fields found in body, expected: {', '.join(keys)}",
            HTTPStatus.BAD_REQUEST,
        )

    user = User(**{key: func(body[key]) for key, func in keys.items()})
    users_repository.add(user)
    return user.as_dict(), HTTPStatus.CREATED


@bp.post("/api/users/token")
def get_token() -> Response:
    """
    Given the email and password, authenticates an user

    Returns:
        Response: detailed message whether auth has been successful or not
    """
    body = request.get_json() or {}
    keys = {
        "email": str.lower,
        "password": sha256,
    }

    if any(key not in body for key in keys):
        return create_error(
            f"not all required fields found in body, expected: {', '.join(keys)}",
            HTTPStatus.BAD_REQUEST,
        )

    params = {key: func(body[key]) for key, func in keys.items()}
    matched = filter(
        lambda user: user.email == params["email"]
        and user.password == params["password"],
        users_repository.items.values(),
    )

    user = next(matched, None)
    if not user:
        return create_error(
            "could not authenticate user, wrong email or password",
            HTTPStatus.FORBIDDEN,
        )

    return {"message": f"logged in as '{user.name}'"}, HTTPStatus.OK
