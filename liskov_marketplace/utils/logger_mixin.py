import logging
from abc import ABCMeta
from logging import Logger


class LoggerMixin(metaclass=ABCMeta):
    """
    Mixin to enable out-of-the-box logging
    """

    def __init__(self) -> None:
        """
        LoggerMixin constructor
        """
        self._log = None

    @property
    def log(self) -> Logger:
        """
        Getter for the logger instance

        Returns:
            Logger: instance of logger
        """
        if not self._log:
            self._log = logging.getLogger(
                f"{self.__class__.__module__}.{self.__class__.__name__}"
            )

        return self._log
