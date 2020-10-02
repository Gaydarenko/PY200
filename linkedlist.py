from typing import Any, Optional
from node import Node
import Drivers


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
        # self.sd = None

    def __len__(self):
        """
        Redetermine command len
        :return: length LinkedList
        """
        return self.__len

    def __repr__(self):
        return '<->'.join(str(n) for n in self)

    @staticmethod
    def verification_index(index: int) -> None:
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

    def __iter__(self, current_node=None):
        """
        Redetermine iterator
        :return: next node
        """
        if not current_node:
            current_node = self.__head

        while current_node:
            yield current_node.value
            current_node = current_node.next

    def _node_iter(self):
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node
            current_node = current_node.next

    def __reversed__(self, current_node=None):
        """
        Redetermine reversed iterator
        :return: previous node
        """
        if not current_node:
            current_node = self.__tail

        while current_node:
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

    def find(self, node: Optional["Node"]) -> int:
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

    def remove(self, node: Optional["Node"]) -> None:
        """
        Remove the first occurrence of the specified node.
        :param node: node value
        :return: ValueError if the value is not found
        """

        if node.value == self.__head.value:
            self.__head = self.__head.next

        else:
            current_node = self.__head
            for _ in range(self.__len - 2):
                if current_node.next.value == node.value:
                    next_node = current_node.next
                    next_node = next_node.next
                    current_node.next = next_node
                    next_node.prev = current_node
                    break
                current_node = current_node.next

            else:
                if node.value == self.__tail.value:
                    self.__tail = self.__tail.prev
                else:
                    raise ValueError

        self.__len -= 1

    def delete(self, index: int) -> None:
        """
        Delete node with index
        :param index: node index
        :return: None
        """
        if index not in range(self.__len):
            raise IndexError

        if index == 0:
            self.__head = self.__head.next
            self.__head.prev = None

        elif index == self.__len - 1:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        else:
            current_node = self.__head
            for _ in range(index - 1):
                current_node = current_node.next

            next_node = current_node.next
            next_node = next_node.next
            current_node.next = next_node
            next_node.prev = current_node

        self.__len -= 1

    def save(self) -> None:
        """
        Transforms node list to dictionary with nodes for save in some file.
        :return: dict
        """
        linked_list = {}
        for node in self._node_iter():
            linked_list[id(node)] = {
                "value": node.value,
                "next_node": id(node.next) if node.next else None,
                "prev_node": id(node.prev) if node.prev else None   # для того чтобы можно было реализовать проход
                                                                # с конца. Сейчас это не нужно, это памятка для меня.
            }
        self.sd.write({"head": id(self.__head), "nodes": linked_list, "tail": id(self.__tail)})

    def load(self):     # , new_nodes: dict):
        """
        Load data from some source and create new linked list.
        # :param new_nodes: dictionary with nodes
        :return: None
        """
        self.clear()
        new_nodes = self.sd.read()
        id_head = new_nodes["head"]

        for _ in range(len(new_nodes["nodes"])):
            node = new_nodes["nodes"].pop(str(id_head))
            # title = node["value"]["title"]
            # author = node["value"]["author"]
            # genre = node["value"]["genre"]
            self.append(node["value"])
            id_head = node["next_node"] if node["next_node"] else None

    def set_structure_driver(self, structure_driver):
        self.sd = structure_driver


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append({1: 1})
    l1.append({2: 2})
    l1.insert(12, 3)
    # l1.append(4)
    # l1.insert(9, 5)
    # l1.insert(0, 0)
    # l1.insert(1, 99)
    # print(dir(l1))
    # # print(l1)
    # a = iter(l1)

    print(l1)

    # l1.save()
    # print(d1)
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # l1.clear()
    # l1.load(d1)
    # print(l1)

    # driver_name = input("Please enter driver name > ")
    builder = Drivers.SDFabric().get_sd_driver("JSONFileDriver")
    sd = builder.build()
    #
    l1.set_structure_driver(sd)
    l1.save()
    # l1.load()
    print(l1)
    # print(next(l1.__iter__()))
    # print(next(l1.__iter__()))

    # obj = {
    #     "a": [
    #         {
    #             "a": 1,
    #             "b": True,
    #             "c": "some string"
    #         },
    #         {
    #             "afff": None,
    #             "caaa": "some string 2"
    #         }
    #     ],
    #     "value": (1, 2, 3)
    # }
    # sd.write(obj)

    # for _ in range(len(l1)):
    #     print(next(a))
    # print('')

    # print('!!!!!!')
    # print(l1.find(Node(99)))
    # print(l1.find(Node(0)))
    # print(l1.find(Node(5)))
    # print(l1.find(Node(6)))
    #
    # print(l1, f'len = {len(l1)}')
    # l1.remove(Node(4))
    # print(l1, f'len = {len(l1)}')
    # l1.remove(Node(3))
    # print(l1, f'len = {len(l1)}')

    # l1.clear()
    # print(len(l1))
    # l1.delete(6)
    # print(l1)

    # print(reversed(next(l1)))

    # for value in l1:
    #     print(value)
