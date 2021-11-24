from dataclasses import dataclass

from liskov_marketplace.models.entity import Entity


@dataclass
class User(Entity):
    """
    User entity model
    """

    balance: float = 0.0

    def as_dict(self) -> dict:
        """
        Gets this user instance as dict

        Returns:
            dict: this instance's representation as dict
        """
        return {
            "id": self.id,
        }
