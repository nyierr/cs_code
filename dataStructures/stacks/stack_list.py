class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

class StackL:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.empty():
            return "[]"

        current = self.top
        txt = "[" + str(current.get_data())
        while(current.get_next()):
            current = current.get_next()
            txt += ", " + str(current.get_data())

        return txt + "]"

    def empty(self):
        return 0 == self.size

    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self):
        if self.empty():
            raise ValueError("Stack underflow")            
        
        removed = self.top
        self.top = self.top.get_next()
        self.size -= 1

        return removed.get_data()

    def peek(self):
        if self.empty():
            raise ValueError("Stack underflow")
        return self.top.get_data()

print("Testing stack")
sl = StackL()
sl.push(5)
sl.push(3)
sl.push(1)
print("Added some elements: " + str(sl))

print("Peek: " + str(sl.peek()))

sl.pop()
sl.pop()
print("Removed some elements: " + str(sl))

sl.pop()
print("Empty stack: " + str(sl))