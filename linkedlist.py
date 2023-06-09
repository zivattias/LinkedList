# 'annotations' enables class typing within its own class
from __future__ import annotations

# advanced typing - Optional[Type] = Type | None, Iterable = iterator protocol implemented
from typing import Optional, Iterable


class Node:
    def __init__(
        self,
        value=None,
        next_node: Optional[Node] = None,
        previous_node: Optional[Node] = None,
    ):
        self.__value = value
        self.__next = next_node
        self.__previous = previous_node

    @property
    def next(self) -> Optional[Node]:
        return self.__next

    @next.setter
    def next(self, node: Node):
        self.__next = node

    @property
    def previous(self) -> Optional[Node]:
        return self.__previous

    @previous.setter
    def previous(self, node: Node):
        self.__previous = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class LinkedList:
    def __init__(self, iterable: Optional[Iterable] = None):
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        self.__len: int = 0

        if iterable is not None:
            for item in iterable:
                self.append(item)

        self.__current_node: Optional[Node] = self.__head

    @property
    def head(self) -> Optional[Node]:
        return self.__head

    @head.setter
    def head(self, node: Node):
        self.__head = node

    @property
    def tail(self) -> Optional[Node]:
        return self.__tail

    @tail.setter
    def tail(self, node: Node):
        self.__tail = node

    @property
    def len(self) -> int:
        return self.__len

    @len.setter
    def len(self, value: int):
        self.__len = value

    # Iterator protocol implementation:
    def __iter__(self):
        self.__current_node = self.head
        return self

    def __next__(self):
        if self.__current_node is None:
            raise StopIteration

        value = self.__current_node.value
        self.__current_node = self.__current_node.next
        return value

    # Iterator length:
    def __len__(self):
        return self.len

    # Append implementation:
    def append(self, value):
        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value

        if self.head is None:
            self.head = new_node
        else:
            if self.tail is None:
                self.head.next = new_node
                new_node.previous = self.head
            else:
                self.tail.next = new_node
                new_node.previous = self.tail

        self.tail = new_node
        self.len += 1

    # Insert node at a specific index:
    def insert(self, value, index: int):
        if index < 0 or index > len(self):
            raise IndexError("Insertion index out of range")

        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next = new_node
            # new_node.next = current_node.next = None for tails, hence checking if it's not the tail:
            if new_node.next is not None:
                new_node.next.previous = new_node
            # if it is, update the tail:
            else:
                self.tail = new_node

        self.len += 1

    # Remove node from a specific index:
    def remove(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("Removal index out of range")

        if index == 0:
            node = self.head
            self.head = node.next
            del node
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.previous.next = current_node.next
            # current_node.next = None for tails, hence checking if it's not the tail:
            if current_node.next is not None:
                current_node.next.previous = current_node.previous
            # if it is, update the tail:
            else:
                self.tail = current_node.previous
            del current_node

        self.len -= 1

    # Returns a new LinkedList with all the elements from the original LinkedList, reversed - doubly
    def reverse(self: LinkedList) -> LinkedList:
        reversed_list = LinkedList()
        current = self.tail

        while current is not None:
            reversed_list.append(current.value)
            current = current.previous

        return reversed_list

    # Returns a new LinkedList with all the elements from the original LinkedList, reversed - singly - WIP
    def singly_reverse(self: LinkedList) -> LinkedList:
        reversed_list = LinkedList()
        current = self.head

        while current is not None:
            new_node = Node(current.value)

            new_node.next = reversed_list.head
            reversed_list.head = new_node

            current = current.next

        return reversed_list

    # Combine 2 (two) LinkedLists into 1 (one) new LinkedList, available for variable assignment
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError(
                f"unsupported operand type(s) for +: 'LinkedList' and '{type(other).__name__}'"
            )
        new_list = LinkedList()

        for node in self:
            new_list.append(node)
        for node in other:
            new_list.append(node)

        return new_list
