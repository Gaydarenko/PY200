from typing import Any, Optional
from node import Node


class LinkedList:
    """
    This class implements linked list
    """

    def __init__(self):
        """
        Variables initialization
        """
        self.__head = self.__tail = None
        self.__len = 0

    def __len__(self):
        """
        Redetermine command len
        :return: length LinkedList
        """
        return self.__len

    def __repr__(self):
        return '<->'.join(str(n) for n in self)

    # @staticmethod
    def verification_index(self, index: int) -> None:
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
        self.verification_index(index)
        insert_node = Node(value)

        if not self.__len or index >= self.__len:         # пустой список или индекс за пределами списка
            self.append(value)
        elif index == 0:
            insert_node.next = self.__head
            self.__head.prev = insert_node
            self.__head = insert_node
            self.__len += 1
        else:
            current_node = self.__head
            for i in range(self.__len):
                if i == index - 1:  # определение ноды, после которой необходимо произвести вставку
                    insert_node.next = current_node.next    # перенапрвление прямой ссылки
                    current_node.next = insert_node

                    insert_node.prev = current_node  # перенаправление обратной ссылки

                    current_node = insert_node.next     # перенос фокуса внимания на ноду после вставки
                    current_node.prev = insert_node

                    self.__len += 1
                    break

                current_node = current_node.next

    def append(self, value: Any) -> None:
        """
        Add Node to the tail of LinkedList
        :param value: inserting node
        :return: None
        """
        append_node = Node(value)

        if not self.__len:
            self.__head = append_node
            self.__tail = self.__head
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

    def __reversed__(self):
        """
        Redetermine reversed iterator
        :return: previous node
        """
        current_node = self.__tail
        for _ in range(self.__len):
            yield current_node.value
            current_node = current_node.prev

    def clear(self) -> None:
        """
        Clear LinkedList
        :return: None
        """
        self.__head = None
        self.__tail = None
        self.__len = 0

    def find(self, node: Node) -> int:
        """
        Finds the first occurrence of the specified node.
        :param node: node value
        :return: node index or -1 if the value is not found
        """
        for current_node in enumerate(self):
            if current_node[1] == node.value:
                return current_node[0]
        else:
            return -1

    def remove(self, node: Node):
        """
        Remove the first occurrence of the specified node.
        :param node: node value
        :return: ValueError if the value is not found
        """

        if node.value == self.__head.value:
            self.__head = self.__head.next

        elif node.value == self.__tail.value:
            self.__tail = self.__tail.prev

        else:
            current_node = self.__head
            for _ in range(self.__len - 2):
                if current_node.next.value == node.value:
                    next_node = current_node.next
                    next_node = next_node.next
                    current_node.next = next_node
                    next_node.prev = current_node
                    self.__len -= 1
                    break
                current_node = current_node.next
            else:
                raise ValueError

        self.__len -= 1

    def delete(self, index):
        if index not in range(self.__len):
            raise IndexError

        if index == 0:
            self.__head = self.__head.next

        elif index == self.__len - 1:
            self.__tail = self.__tail.prev

        else:
            current_node = self.__head
            for _ in range(index - 1):
                current_node = current_node.next

            next_node = current_node.next
            next_node = next_node.next
            current_node.next = next_node
            next_node.prev = current_node

        self.__len -= 1


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.insert(12, 3)
    l1.append(4)
    l1.insert(9, 5)
    l1.insert(0, 0)
    l1.insert(1, 99)
    print(dir(l1))
    print(l1)
    a = iter(l1)

    # for _ in range(len(l1)):
    #     print(next(a))
    # print('')

    print('!!!!!!')
    print(l1.find(Node(99)))
    print(l1.find(Node(0)))
    print(l1.find(Node(5)))
    print(l1.find(Node(6)))

    # l1.remove(Node(5))
    print(l1)
    # l1.clear()
    print(len(l1))
    l1.delete(6)
    print(l1)




    # print(reversed(next(l1)))

    # for value in l1:
    #     print(value)
