# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-27-2022
# Description: A linked list that contains recursive add, remove, contains, insert and reverse methods. Also has a
# recursive to_plain_list method that takes no parameters and returns a list that has the same values.

class Node:
    """Represents a node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A linked list that...."""

    def __init__(self):
        self._head = None

    def __add__(self, val):
        """Add method for nodes in linked list containing val to end of the linked list"""
        if self._head is None:
            self._head = Node(val)

        else:
            curr = self._head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

    def remove(self, val):
        """Remove method for nodes containing val within linked list"""
        if self._head is None:
            return

        if self._head.data == val:
            self._head = self._head.next

        else:
            curr = self._head
            while curr is not None and curr.data != val:
                previous = curr
                curr = curr.next
                if curr is not None:
                    previous.next = curr.next

    def display(self):
        """Displays the values in a linked list by printing them"""
        curr = self._head
        while curr is not None



