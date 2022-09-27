"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T

def bf_order_D_L(D: deque([T]), L: list[int]):
    """Just a recursive function to understand
    Not the real working function"""
    N = deque([])
    for t in D:
        if(t!=None):
            N.append(t.left)
            N.append(t.right)
            L.append(t.val)
    if (N != deque([])):
        bf_order_D_L(N, L)




def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """
    D = deque([])
    L = []
    if(t!=None):
        D.append(t)
        while D:
            t = D.popleft()
            if(t.left!=None):
                D.append(t.left)
            if(t.right!=None):
                D.append(t.right)
            L.append(t.val)
                
    return  L
