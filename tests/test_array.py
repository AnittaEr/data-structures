from unittest import TestCase

from data_structures.array import Array

# from ds import Array


class TestArray(TestCase):
    def test_append(self):
        array = Array()
        array.append(3)
        array.append(-1)
        self.assertEqual(array.append(5), None)

    def test_size(self):
        array = Array()

        for i in range(5):
            array.append(i)

        self.assertEqual(array.size, 5)
        array.clear()
        i = 0
        while i < 300:
            array.append("s")
            i += 1

        self.assertEqual(len(array), 300)
        print(array)

    def test_pop(self):
        array = Array()
        for i in range(5):
            array.append(i)

        self.assertEqual(array.pop(), 4)

    def test_clear(self):
        array = Array()
        for i in range(5):
            array.append(i)

        self.assertEqual(array.clear(), None)
