# LinkedList() consits multiple Node()s that map to each other.

# 'annotations' enables class typing within its own class
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value=None):
        self._value = value
        self.__next: Optional[Node] = None
        self.__previous: Optional[Node] = None

    def __str__(self) -> str:
        return f"<Node: {self._value}>"

    @property
    def next(self) -> Optional[Node]:
        return self.__next

    @property
    def previous(self) -> Optional[Node]:
        return self.__previous


class LinkedList:
    def __init__(self, iterable: Optional[LinkedList] = None) -> None:
        if iterable is None:
            self.__head: Optional[Node] = None
            self.__tail: Optional[Node] = self._head
            self.__len: int = 0
        elif isinstance(iterable, LinkedList):
            self._head, self._tail, self._len = (
                iterable.head,
                iterable.tail,
                iterable.len,
            )
        else:
            raise TypeError()

    @property
    def head(self) -> Optional[Node]:
        return self.__head

    @property
    def tail(self) -> Optional[Node]:
        return self.__tail

    @property
    def len(self) -> int:
        return self.__len
