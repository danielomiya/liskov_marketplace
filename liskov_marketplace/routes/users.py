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
    body = request.get_json() or {}
    keys = {
        "name": identity,
        "birth_date": lambda d: datetime.strptime(d, "%Y-%m-%d"),
        "cpf_cnpj": identity,
        "email": identity,
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
