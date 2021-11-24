from http import HTTPStatus
from typing import Any, Dict, Tuple

JsonObject = Dict[str, Any]
Response = Tuple[JsonObject, HTTPStatus]
