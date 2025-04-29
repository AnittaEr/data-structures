from unittest import TestCase

from data_structures.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(TestCase):
    def test_insert(self):
        binarySearchTree = BinarySearchTree()
        for i in range(3):
            binarySearchTree.insert(i)
            self.assertEqual(binarySearchTree.insert(i), None)

        self.assertEqual(binarySearchTree.insert(3), None)

    def test_find(self):
        binarySearchTree = BinarySearchTree()
        binarySearchTree.insert(1)
        binarySearchTree.insert(3)
        binarySearchTree.insert(5)

        self.assertEqual(binarySearchTree.find(3), 3)

    def test_delete(self):
        binarySearchTree = BinarySearchTree()
        for i in range(5):
            binarySearchTree.insert(i)

        for i in range(5):
            assert binarySearchTree.delete(i) is None
            assert binarySearchTree.find(i) == -1

        assert binarySearchTree.delete(6) == -1

    def test_delete2(self):
        binarySearchTree = BinarySearchTree()
        for i in range(10):
            binarySearchTree.insert(i)

        assert binarySearchTree.delete(100) == -1
        assert binarySearchTree.delete(9) is None
        assert binarySearchTree.find(6) == 6
        assert binarySearchTree.delete(4) is None
        assert binarySearchTree.find(6) == 6
        assert binarySearchTree.find(2) == 2
        assert binarySearchTree.delete(4) == -1

    def test_delete_when_delete_entire_tree(self):
        binarySearchTree = BinarySearchTree()
        binarySearchTree.insert(10)

        assert binarySearchTree.find(10) == 10
        assert binarySearchTree.delete(10) is None
        assert len(binarySearchTree) == 0
        assert binarySearchTree.find(10) == -1

    def test_size(self):
        binarySearchTree = BinarySearchTree()
        for i in range(5):
            binarySearchTree.insert(i)

        assert len(binarySearchTree) == 5

    def test_preorder_traversal(self):
        binarySearchTree = BinarySearchTree()
        for i in range(5):
            binarySearchTree.insert(i)

        assert binarySearchTree.preorder() == [0, 1, 2, 3, 4]
        for i in range(5):
            assert binarySearchTree.delete(i) is None

        assert binarySearchTree.preorder() is None
        binarySearchTree.insert(7)
        binarySearchTree.insert(1)
        binarySearchTree.insert(10)
        binarySearchTree.insert(3)
        binarySearchTree.insert(2)
        binarySearchTree.insert(5)
        binarySearchTree.insert(9)

        assert binarySearchTree.preorder() == [7, 1, 3, 2, 5, 10, 9]

    def test_inorder_traversal(self):
        binarySearchTree = BinarySearchTree()
        assert binarySearchTree.inorder() is None
        binarySearchTree.insert(7)
        binarySearchTree.insert(1)
        binarySearchTree.insert(2)
        binarySearchTree.insert(10)
        binarySearchTree.insert(3)
        binarySearchTree.insert(9)
        binarySearchTree.insert(5)
        assert binarySearchTree.inorder() == [1, 2, 3, 5, 7, 9, 10]

    def test_postorder_traversal(self):
        binarySearchTree = BinarySearchTree()
        assert binarySearchTree.postorder() is None
        binarySearchTree.insert(7)
        binarySearchTree.insert(1)
        binarySearchTree.insert(10)
        binarySearchTree.insert(3)
        binarySearchTree.insert(2)
        binarySearchTree.insert(5)
        binarySearchTree.insert(9)

        assert binarySearchTree.postorder() == [2, 5, 3, 1, 9, 10, 7]

    def test_traverse_bst(self):
        binarySearchTree = BinarySearchTree()
        binarySearchTree.insert(7)
        binarySearchTree.insert(5)
        binarySearchTree.insert(4)
        binarySearchTree.insert(6)
        binarySearchTree.insert(9)
        binarySearchTree.insert(10)
        binarySearchTree.insert(8)

        assert binarySearchTree.bfs() == [7, 5, 9, 4, 6, 8, 10]
