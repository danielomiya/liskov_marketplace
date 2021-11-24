from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from liskov_marketplace.models.entity import Entity

T = TypeVar("T", Entity, object)


class BaseRepository(Generic[T], metaclass=ABCMeta):
    """
    Base class to implement repositories
    """

    @abstractmethod
    def add(self, item: T) -> int:
        """
        Adds an item to the repository

        Args:
            item (T): item to be added

        Returns:
            int: id of item added
        """
        raise NotImplementedError()

    @abstractmethod
    def get(self, _id: int, *, fallback: T = None) -> T:
        """
        Obtains an item from the repository or the fallback in case it is not found

        Args:
            _id (int): id of the item
            fallback (T, optional): fallback if the item is not found. Defaults to None.

        Returns:
            T: item
        """
        raise NotImplementedError()
