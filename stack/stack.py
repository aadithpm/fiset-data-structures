class Stack():
    def __init__(self):
        self.data = []
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        self.length -= 1
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.data[self.length - 1]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        stack_str = '['
        for i in range(self.length - 1):
            stack_str += str(self.data[i]) + ', '
        return stack_str + str(self.data[self.length - 1]) + ']'
