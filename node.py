from typing import Any
from weakref import ref


class Node:
    def __init__(self, value: Any, next_=None, prev_=None):
        """
        Создаем новый узел для двусвязного списка

        :param value:
        :param next_: node class Node
        :param prev_: node class Node
        """
        self.__next = next_  # class Node
        self.__prev = prev_
        self.value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if not isinstance(next_, (Node, type(None))):
            raise TypeError

        self.__next = next_

    @property
    def prev(self):
        return self.__prev() if self.__prev is not None else None

    @prev.setter
    def prev(self, prev_):
        if not isinstance(prev_, Node):
            raise TypeError

        self.__prev = ref(prev_)

    def __str__(self):
        return f"{repr(self.__prev)} << Value: {self.value} >> {repr(self.__next)}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    # def __repr__(self):
    #     return f"{self.__class__.__name__}({self.value}, {self.next.value}, {self.prev.value})"
