class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

class QueueL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.head
        txt = "[" + str(current.get_data())

        while(current.get_next()):
            current = current.get_next()
            txt += ", " + str(current.get_data())

        return txt + "]"

    def empty(self):
        return 0 == self.size

    def enqueue(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        
        self.size += 1

    def dequeue(self):
        if self.head == None:
            return None

        removed = self.head
        self.head = removed.get_next()
        if self.size == 1:
            self.tail = removed.get_next()

        self.size -= 1
        return removed.get_data()

    def search(self, data):
        if self.head == None:
            return False

        current = self.head
        while(current.get_next()):
            if data == current.get_data():
                return True
            current = current.get_next()

        return data == current.get_data()

print("Testing queue ")
ql = QueueL()
ql.enqueue(5)
ql.enqueue(3)
ql.enqueue(7)
print("Added some data: " + str(ql))
print("Size: " + str(len(ql)))

ql.dequeue()
print("Dropped some data: " + str(ql))
print("Size: " + str(len(ql)))

ql.dequeue()
print("Dropped some data: " + str(ql))
print("Size: " + str(len(ql)))

ql.enqueue(1)
print("Added some data: " + str(ql))
print("Size: " + str(len(ql)))

ql.dequeue()
print("Dropped some data: " + str(ql))
print("Size: " + str(len(ql)))

print("Looking for 1: "+ str(ql.search(1)))
print("Looking for 2: "+ str(ql.search(2)))