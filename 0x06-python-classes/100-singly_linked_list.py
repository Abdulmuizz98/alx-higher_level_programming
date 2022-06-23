#!/usr/bin/python3
"""Node module

Contains the definition of a node class.

"""


class Node:
    """Definition of a node object.

    Defines a node of a singly linked list.

    """
    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): the data contained in the node.
            next_node (node): the pointer to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter and setter for data property """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter and setter for the next node property """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list data structure """
    def __init__(self):
        """Initialize the singly linked list """
        self.__head = None

    def __str__(self):
        """String rep of the sll """
        current = self.__head
        res = ""
        while current is not None:
            if current.next_node is None:
                res += str(current.data)
            else:
                res += str(current.data) + "\n"
            current = current.next_node
        return res

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
           Args:
               value (int): the data value of the new node
        """
        new_node = Node(value)
        current = self.__head
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        while current.next_node is not None:
            if value < current.next_node.data:
                break
            current = current.next_node
        temp = current.next_node
        current.next_node = new_node
        new_node.next_node = temp
