import ctypes


class Array:
    INITIAL_SIZE = 5
    RESIZE_MULTIPLIER = 2
    RESIZE_DIVISOR = 1 / 2

    def __init__(self):
        ArrayType = ctypes.py_object * self.INITIAL_SIZE
        self.arr = ArrayType()
        self.size = 0
        self.capacity = 5

    def append(self, item):
        if self.size >= self.capacity:
            self._resizeUp()
        self.arr[self.size] = item
        self.size += 1

    def _resizeUp(self):
        prevArray = self.arr
        NewArrayType = ctypes.py_object * (self.capacity * self.RESIZE_MULTIPLIER)
        self.arr = NewArrayType()

        for i in range(self.capacity):
            self.arr[i] = prevArray[i]

        self.capacity = self.capacity * self.RESIZE_MULTIPLIER

    def pop(self):
        if self.size < 0.5 * self.capacity:
            self._resizeDown()
        res = self.arr[-1]
        self.size -= 1
        return res

    def _resizeDown(self):
        prevArray = self.arr
        NewArrayType = ctypes.py_object * (self.capacity * self.RESIZE_DIVISOR)
        self.arr = NewArrayType()
        self.capacity = self.capacity * self.RESIZE_DIVISOR
        for i in range(self.capacity):
            self.arr[i] = prevArray[i]

    def clear(self):
        self.size = 0
        ArrayType = ctypes.py_object * 5
        self.arr = ArrayType()
        self.capacity = 5

    def __len__(self):
        return self.size
