class StackA:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1

    def __len__(self):
        return self.top + 1

    def __str__(self):
        if self.empty():
            return "[]"
        
        txt = "[" + str(self.stack[self.top])
        for i in range(self.top - 1, -1, -1):
            txt += ", " + str(self.stack[i])

        return txt + "]"

    def empty(self):
        return -1 == self.top

    def full(self):
        return self.top == self.capacity - 1

    def push(self, data):
        if self.full():
            raise ValueError("Stack overflow")
        
        if self.empty():
            self.top = 0
        else:
            self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.empty():
            raise ValueError("Stack underflow")

        removed = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return removed

    def peek(self):
        if self.empty():
            raise ValueError("Stack underflow")
        return self.stack[self.top]

print("Testing a stack")
sa = StackA(4)
sa.push(3)
sa.push(5)
sa.push(1)
sa.push(7)
print("Added some elements: " + str(sa))

print("Peek: " + str(sa.peek()))

sa.pop()
print("Popped: " + str(sa))

sa.pop()
sa.pop()
print("Poppped more: " + str(sa))