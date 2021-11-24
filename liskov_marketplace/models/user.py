from dataclasses import dataclass
from datetime import datetime

from liskov_marketplace.models.entity import Entity


@dataclass
class User(Entity):
    """
    User entity model
    """

    name: str = None
    birth_date: datetime = None
    cpf_cnpj: str = None
    email: str = None
    phone: str = None
    password: bytes = None

    def as_dict(self) -> dict:
        """
        Gets this user instance as dict

        Returns:
            dict: this instance's representation as dict
        """
        return {
            "id": self.id,
            "name": self.name,
            "birth_date": self.birth_date.strftime("%Y-%m-%d"),
            "cpf_cnpj": self.cpf_cnpj,
            "email": self.email,
            "phone": self.phone,
        }
