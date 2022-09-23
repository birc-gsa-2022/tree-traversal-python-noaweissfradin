"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T

def in_order_L(t: T | None, L: list[int]):
    if(t!=None):
        in_order_L(t.left,L)
        L.append(t.val)
        in_order_L(t.right,L)


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    L = []
    in_order_L(t, L)

    return L
