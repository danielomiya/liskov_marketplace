from http import HTTPStatus

from liskov_marketplace.models.user import User
from liskov_marketplace.repositories.base_repository import BaseRepository
from liskov_marketplace.repositories.in_memory_repository import InMemoryRepository
from liskov_marketplace.typing import Response
from liskov_marketplace.utils.http_error import create_error
from flask import Blueprint, request

bp = Blueprint("users", __name__)
users_repository: BaseRepository[User] = InMemoryRepository()


@bp.post("/api/users")
def create_user():
    user = request.get_json() or {}
