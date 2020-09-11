from typing import Any
from node import Node


class LinkedList:
    """
    This class implements linked list
    """

    def __init__(self):
        """
        Variables initialization
        """
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        """
        Redetermine command len
        :return: length LinkedList
        """
        return self.__len

    # @staticmethod
    def verification(self, index: int) -> None:
        """
        Verification of requirements for index
        :param index: Node position in LinkedList
        :return: None
        """
        if not isinstance(index, int):
            raise IndexError('Index must be only int')
        if index < 0:
            raise IndexError('Index must be only positive or zero')

    def insert(self, index: int, value: Any) -> None:
        """
        Insert Node to any place of LinkedList
        :param index: position of node
        :param value: inserting node
        :return: None
        """
        self.verification(index)
        insert_node = Node(value)

        if self.__len == 0:         # пустой список
            self.__head = insert_node
            self.__tail = self.__head
            self.__len += 1
        elif index > self.__len:    # индекс за пределами списка
            self.append(value)
        # TODO insert in center     # индекс в середине списка

    def append(self, value: Any) -> None:
        """
        Add Node to the tail of LinkedList
        :param value: inserting node
        :return: None
        """
        append_node = Node(value)

        if not self.__len:
            self.insert(0, value)
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node
            self.__tail = append_node
            self.__len += 1

    def __iter__(self):
        """
        Redetermine iterator
        :return: next node
        """
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.next

    def clear(self) -> None:
        """
        Clear LinkedList
        :return: None
        """
        self.__head = None
        self.__tail = None
        self.__len = 0

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    print(dir(l1))

    for value in l1:
        print(value)
