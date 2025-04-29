from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, item):
        if self.root is None:
            node = Node(item)
            self.root = node
            self.size += 1
            return

        def _recursiveInsert(node, item):
            if node.val > item:
                if node.left is None:
                    node.left = Node(item)
                    print(node.left.val)
                    self.size += 1
                    return
                _recursiveInsert(node.left, item)
            else:
                if node.right is None:
                    node.right = Node(item)
                    print(node.right.val)
                    self.size += 1
                    return
                _recursiveInsert(node.right, item)

        _recursiveInsert(self.root, item)

    def find(self, item):
        if self.root is None:
            return -1

        def _recursiveFind(node, item):
            if node is None:
                return -1

            if node.val == item:
                return node.val

            if item < node.val:
                return _recursiveFind(node.left, item)
            if item > node.val:
                return _recursiveFind(node.right, item)

        return _recursiveFind(self.root, item)

    def delete(self, item):

        if self.root is None:
            return -1

        def minValue(node) -> Node:
            cur = node
            while cur and cur.left:
                cur = cur.left
            return cur

        sizeBeforeDelete = self.size

        def _recursiveDelete(node, item):
            if node is None:
                return None

            if item < node.val:
                node.left = _recursiveDelete(node.left, item)

            elif item > node.val:
                node.right = _recursiveDelete(node.right, item)

            else:
                if node.left is None and node.right is None:
                    self.size -= 1
                    return None

                if node.right:
                    self.size -= 1
                    return node.right

                if node.left:
                    self.size -= 1
                    return node.left

                minNode = minValue(node.right)
                node.val = minNode.val
                node.right = _recursiveDelete(node.right, minNode.val)
            # print(f"node is val {node.val} left {node.left} right {node.right}")
            return node

        self.root = _recursiveDelete(self.root, item)

        if sizeBeforeDelete == self.size:
            return -1
        return None

    def __len__(self):
        return self.size

    def preorder(self):
        self.result = []

        def _traverse(node, result):
            if not node:
                return None
            result.append(node.val)
            _traverse(node.left, result)
            _traverse(node.right, result)

            return result

        print("result", self.result)
        return _traverse(self.root, self.result)

    # inorder traversal in bst is sorted array
    def inorder(self):
        self.result = []

        def _traverse(node, result):
            if not node:
                return None

            _traverse(node.left, result)
            result.append(node.val)
            _traverse(node.right, result)
            return result

        return _traverse(self.root, self.result)

    def postorder(self):
        self.result = []

        def _traverse(node, result):
            if not node:
                return None

            _traverse(node.left, result)
            _traverse(node.right, result)
            result.append(node.val)
            return result

        return _traverse(self.root, self.result)

    def bfs(self):
        self.result = []

        def _traverse(node, result):
            if not node:
                return None
            queue = deque()
            queue.append(node)
            while len(queue) > 0:
                for _i in range(len(queue)):
                    cur = queue.popleft()
                    result.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)

            return result

        return _traverse(self.root, self.result)

    # def height()
    #
    # def min()
    # def max()
    #


# if __name__ == "__main__":
#     tree = BinarySearchTree()
#     tree.insert(7)
#     tree.insert(1)
#     tree.insert(10)
#     tree.insert(3)
#     tree.insert(2)
#     tree.insert(5)
#     tree.insert(9)

#     tree.preorder()
