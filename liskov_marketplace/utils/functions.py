from typing import TypeVar

T = TypeVar("T")


def identity(x: T) -> T:
    """
    Identity function

    Args:
        x (T): some value

    Returns:
        T: value itself
    """
    return x
