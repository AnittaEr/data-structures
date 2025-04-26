class Stack:
    def __init__(self):
        self._arr = []
        self.size = 0

    def push(self, item):
        self._arr.append(item)
        self.size += 1

    def pop(self):
        if self._arr:
            self.res = self._arr.pop()
            print(self.res)

            self.size -= 1
            return self.res
        return -1

    def __len__(self):
        return self.size

    def peek(self):
        if self._arr:
            return self._arr[-1]
        return -1
