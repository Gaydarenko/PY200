import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()

    def test_insert_empty_list(self):
        self.list_.insert(2, 3)
        self.assertEqual(len(self.list_), 1)
        self.test_clear_list()
        self.list_.insert(0, 3)
        self.assertEqual(len(self.list_), 1)
        self.test_clear_list()

    def test_clear_list(self):
        self.list_.clear()
        self.assertEqual(len(self.list_), 0)

    def test_append_to_list(self):
        self.list_.append(6)
        self.assertEqual(len(self.list_), 1)
        self.list_.append(1)
        self.assertEqual(len(self.list_), 2)


if __name__ == "__main__":
    unittest.main()
