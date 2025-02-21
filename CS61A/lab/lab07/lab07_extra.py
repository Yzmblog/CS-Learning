""" Optional Questions for Lab 07 """

from lab07 import *

# Q9
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link.rest is Link.empty:
        return
    elif link.second==value:
        link.rest=link.rest.rest
        remove_all(link,value)
    else:
        remove_all(link.rest,value)
    

# Q10
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link.rest is Link.empty:
        if isinstance(link.first,int):
            link.first=fn(link.first)
        else:
            deep_map_mut(fn, link.first)
        return
    else:
        if isinstance(link.first,int):
            link.first=fn(link.first)
        else:
            deep_map_mut(fn, link.first)
        deep_map_mut(fn,link.rest)

# Q11
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    l=link
    while link.rest!=Link.empty:
        if link.rest==l:
            return True
        link.rest=link.rest.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return False
    slow, fast = link, link.rest
    while fast != Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:
            return True
        slow, fast = slow.rest, fast.rest.rest
    return False
# Q12
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():
        a = [b.label for b in t.branches][::-1]
        for bra, label_r in zip(t.branches, a):
            bra.label = label_r
            if not bra.is_leaf():
                for bra_2 in bra.branches:
                    reverse_other(bra_2)

