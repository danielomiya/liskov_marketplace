from collections.abc import Sized
from typing import Dict

from liskov_marketplace.repositories.base_repository import BaseRepository, T
from liskov_marketplace.utils.logger_mixin import LoggerMixin


class InMemoryRepository(BaseRepository[T], LoggerMixin, Sized):
    """
    Repository implementation in-memory
    """

    def __init__(self) -> None:
        """
        InMemoryRepo constructor
        """
        self.size: int = 0
        self.items: Dict[int, T] = {}
        super().__init__()

    def add(self, item: T) -> int:
        """
        Adds an item to the repository

        Args:
            item (T): item to be added

        Returns:
            int: id of item added
        """
        _id = self.size
        item.id = _id

        self.log.debug("Assgined id %d to '%s'", _id, item.as_dict())

        self.items[_id] = item
        self.size += 1
        return _id

    def get(self, _id: int, *, fallback: T = None) -> T:
        """
        Obtains an item from the repository or the fallback in case it is not found

        Args:
            _id (int): id of the item
            fallback (T, optional): fallback if the item is not found. Defaults to None.

        Returns:
            T: item
        """
        return self.items.get(_id, fallback)

    def __len__(self) -> int:
        """
        Returns how many items are stored in the instance

        Returns:
            int: size of repository
        """
        return self.size
