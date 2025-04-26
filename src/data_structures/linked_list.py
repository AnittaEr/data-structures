class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def insert(self, num):
        node = Node(num)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def delete(self, num):
        # breakpoint()
        if self.head is None:
            raise ValueError()
        if self.head.val == num:
            self.head = self.head.next
            self.size -= 1
            return None

        cur = self.head
        while cur.next:
            if cur.next.val == num:
                cur.next = cur.next.next
                self.size -= 1
                if cur.next is None:
                    self.tail = cur
                return None

            cur = cur.next

        raise ValueError()

    def __len__(self):
        return self.size

    def find(self, value=None, *, compare=None):
        if self.head is None:
            raise ValueError()
        cur = self.head
        while cur:
            if compare is not None:
                if compare(cur.val):
                    return cur
            elif cur.val == value:
                return cur
            cur = cur.next

        raise ValueError()
