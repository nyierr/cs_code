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

class QueueA:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Queue capacity must be greater than 0")

        self.head = None
        self.tail = None
        self.capacity = capacity
        self.queue = [0] * capacity

    def __len__(self):
        return 0 if self.head == None else 1 + self.tail - self.head 

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return (self.head == None) or self.tail < self.head

    def enqueue(self, data):
        if self.tail == self.capacity - 1:
            raise ValueError("Maximum capacity reached")
        
        if self.head == None:
            self.head = 0
            self.tail = 0
        else:
            self.tail += 1

        self.queue[self.tail] = data

    def dequeue(self):
        if self.empty():
            return None

        removed = self.queue[self.head]
        self.queue[self.head] = 0
        
        if self.head == self.tail:
            if self.tail == self.capacity - 1:
                self.head = None
                self.tail = None
                return removed

        self.head += 1
        return removed

    def search(self, data):
        if self.empty():
            return False

        index = self.head
        while(index < self.tail):
            if data == self.queue[index]:
                return True
            index += 1

        return data == self.queue[index]

print("Testing queue (based on singly linked list)")
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

print("\nTesting queue (based on an array)")
qa = QueueA(4)
qa.enqueue(5)
qa.enqueue(3)

print("Added some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.dequeue()
print("Dropped some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.dequeue()
print("Dropped some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.dequeue()
print("Dropped some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.enqueue(7)
print("Added some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.dequeue()
print("Dropped some data: " + str(qa))
print("Size: " + str(len(qa)))

qa.enqueue(1)
print("Added some data: " + str(qa))
print("Size: " + str(len(qa)))

print("Looking for 1: "+ str(qa.search(1)))
print("Looking for 2: "+ str(qa.search(2)))
