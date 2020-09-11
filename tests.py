import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_insert_empty_list(self):
        self.linked_list.insert(2, 3)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 3)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 3)
        self.test_clear_list()
        self.linked_list.insert(0, 4)
        self.assertEqual(len(self.linked_list), 1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 4)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 4)
        self.test_clear_list()

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


if __name__ == "__main__":
    unittest.main()
