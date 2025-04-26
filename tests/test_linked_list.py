from unittest import TestCase

import pytest

from data_structures.linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_insert(self):
        linkedList = LinkedList()
        for i in range(3):
            self.assertEqual(linkedList.insert(i), None)
        self.assertEqual(linkedList.insert("gh"), None)

    def test_delete(self):
        linkedList = LinkedList()
        for i in range(4):
            linkedList.insert(i)
        with pytest.raises(ValueError):
            linkedList.delete(7)
        for i in range(4):
            self.assertEqual(linkedList.delete(i), None)

    def test_size(self):
        linkedList = LinkedList()
        for i in range(3):
            linkedList.insert(i)
            self.assertEqual(len(linkedList), i + 1)

        for i in range(3):
            linkedList.delete(i)
            self.assertEqual(len(linkedList), 2 - i)

    def test_find(self):
        linkedList = LinkedList()
        with pytest.raises(ValueError):
            linkedList.find(1)
        for i in range(3):
            linkedList.insert(i)

        with pytest.raises(ValueError):
            linkedList.find(value=3)
        self.assertEqual(linkedList.find(value=0).val, 0)
        self.assertEqual(linkedList.find(value=1).val, 1)
        self.assertEqual(linkedList.find(value=2).val, 2)
        self.assertEqual(linkedList.find(compare=lambda val: val == 0).val, 0)
        self.assertEqual(linkedList.find(compare=lambda val: val == 1).val, 1)

        linkedList.insert("g")
        self.assertEqual(linkedList.find(value="g").val, "g")
        with pytest.raises(ValueError):
            linkedList.find(7)
        self.assertEqual(linkedList.find(compare=lambda val: val == 2).val, 2)
