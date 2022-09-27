"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T
from collections import deque

def in_order_L(t: T | None, L: list[int]):
    """In-order traversal of a tree
    Recursive function to understand the concept"""
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
    #recursive function
    #in_order_L(t, L)

    #stack function
    S = []
    if(t!=None):
        S.append(t)
        while(S!=[]):
            s = S.pop()
            if(s.left!=None):
                S.append(T(s.val,None,s.right))
                S.append(s.left)
            else:
                L.append(s.val)
                if(s.right!=None):
                    S.append(s.right)

    return L

