from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Entity(metaclass=ABCMeta):
    """
    Base class to implement entities
    """

    id: int = None

    @abstractmethod
    def as_dict(self) -> dict:
        """
        Gets this instance as dict

        Returns:
            dict: this instance's representation as dict
        """
        raise NotImplementedError()
