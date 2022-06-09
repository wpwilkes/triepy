"""
Implementation of trie structure.
"""

from typing import Any, Optional


class _Node:
    """
    Simple trie node structure.
    """

    def __init__(self, char: str, value: Optional[Any] = None) -> None:
        """
        Parameters
        ----------
        char : str
        value :
        """
        self.char = char
        self.value = value
        self.children = {}
        self.end = False

    def __repr__(self) -> str:
        return (f"Node(char={self.char}, value={self.value}, end={self.end})")


class Trie:
    """
    Simple trie structure.
    """

    def __init__(self):
        """
        """
        self._root = _Node('')

    def __delitem__(self, key: str) -> Optional[Any]:
        """
        """
        current, stack = self._root, [self._root]
        for char in key:
            if not current.children.get(char, None):
                return None
            current = current.children[char]
            stack.append(current)

        curr = stack.pop()
        curr.end = False
        rval, curr.value = curr.value, None
        while stack:
            prev, curr = curr, stack.pop()
            if not prev.children:
                curr.children.pop(prev.char)
        return rval

    def __getitem__(self, key: str) -> Optional[Any]:
        """
        """
        current = self._root
        for char in key:
            if not current.children.get(char, None):
                return None
            current = current.children[char]
        return current.value if current.end else None

    def __setitem__(self, key: str, value: Optional[Any] = None) -> None:
        """
        """
        current = self._root
        for char in key:
            if not current.children.get(char, None):
                current.children[char] = _Node(char)
            current = current.children[char]
        current.value = value
        current.end = True
