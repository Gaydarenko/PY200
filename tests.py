import unittest
from linkedlist import LinkedList
from node import Node


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_insert(self):
        self.linked_list.insert(2, 3)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 3)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 3)
        self.test_clear_list()
        self.linked_list.insert(0, 4)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 4)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 4)
        self.linked_list.insert(1, 3)
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(self.linked_list._LinkedList__head.value, 4)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 3)
        self.linked_list.insert(1, 6)
        self.assertEqual(len(self.linked_list), 3)
        self.assertEqual(self.linked_list._LinkedList__head.value, 4)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 3)
        self.assertRaises(IndexError, self.linked_list.insert, -2, 9)

    def test_clear_list(self):
        self.linked_list.clear()
        self.assertEqual(len(self.linked_list), 0)

    def test_append_to_list(self):
        self.linked_list.append(6)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 6)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 6)
        self.linked_list.append(55)
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(self.linked_list._LinkedList__head.value, 6)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 55)

    def test_find(self):
        for i in range(8):
            self.linked_list.append(i)
        for i in range(8):
            self.linked_list.append(i)
        self.assertEqual(0, self.linked_list.find(Node(0)))
        self.assertEqual(7, self.linked_list.find(Node(7)))
        self.assertEqual(-1, self.linked_list.find(Node(8)))

    def test_remove(self):
        for i in range(8):
            self.linked_list.append(i)
        for i in range(8):
            self.linked_list.append(i)
        self.linked_list.remove(Node(2))
        self.assertEqual(9, self.linked_list.find(Node(2)))

    def test_delete(self):
        for i in range(8):
            self.linked_list.append(i)
        for i in range(8):
            self.linked_list.append(i)
        self.linked_list.delete(2)
        self.assertEqual(9, self.linked_list.find(Node(2)))


if __name__ == "__main__":
    unittest.main()
