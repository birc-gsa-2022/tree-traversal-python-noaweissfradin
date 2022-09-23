"""Testing breadth-first traversal"""

from tree import T
from bft import bf_order


def test_in_order() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(bf_order(tree))
    assert res == [2, 1, 4, 3, 5]
    assert list(bf_order(None)) == []

    #just a more complex tree
    tree = T(1, T(1, None, T(3, None, None)), T(4, T(3, T(3, None, None), None), 
    T(5, T(5, None, None), T(5, None, None))))
    res = list(bf_order(tree))
    assert res == [1, 1, 4, 3, 3, 5, 3, 5, 5]

    #a tree with only left leaves
    tree = T(1, T(2, T(3, T(4, T(5, T(6, None, None), None), None), None), None), None)
    res = list(bf_order(tree))
    assert res == [1, 2, 3, 4, 5, 6]

    #a tree with only right leaves
    tree = T(1, None, T(2, None, T(3, None, T(4, None, T(5, None, T(6, None, None))))))
    res = list(bf_order(tree))
    assert res == [1, 2, 3, 4, 5, 6]