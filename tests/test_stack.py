from unittest import TestCase

from data_structures.stack import Stack


class TestStack(TestCase):
    def test_append(self):
        stack = Stack()
        stack.push(3)
        stack.push(-1)
        stack.push(5)
        self.assertEqual(stack.push(10), None)

    def test_size(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.size, 5)

    def test_pop(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)

        self.assertEqual(stack.pop(), 4)

    def test_peek(self):
        stack = Stack()
        for i in range(4):
            stack.push(i)

        self.assertEqual(stack.peek(), 3)
