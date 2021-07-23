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

class CircularQueueL:
    def __init__(self, capacity=1):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.head == None:
            return "[]"

        current = self.head
        txt = "[" + str(current.get_data())

        while(self.__iterate(current)):
            current = current.get_next()
            txt += ", " + str(current.get_data())

        return txt + "]"

    def __iterate(self, node):
        return node.get_next() and node.get_next() != self.head

    def empty(self):
        return 0 == self.size

    def enqueue(self, data):
        if self.size == self.capacity:
            next_node = self.tail.get_next()
            next_node.set_data(data)
            if next_node == self.head:
                self.head = next_node.get_next()
            self.tail = next_node
        else:
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
            elif self.size < self.capacity:
                if self.size == self.capacity - 1:
                    new_node.set_next(self.head)        
                self.tail.set_next(new_node)
            self.tail = new_node
            self.size += 1

    def dequeue(self):
        if self.head == None:
            return None
        
        removed = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = removed.get_next()
            self.tail.set_next(self.head)
        
        self.size -= 1
        return removed.get_data()

    def search(self, data):
        if self.empty():
            return False
        
        current = self.head
        while(self.__iterate(current)):
            if data == current.get_data():
                return True
            current = current.get_next()

        return data == current.get_data()

class CircularQueueA:
    def __init__(self, capacity=1):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity
        self.queue = [0] * capacity

    def __str__(self):
        if self.empty():
            return "[]"
        
        current = self.head
        txt = "[" + str(self.queue[current])

        processed = 1
        while(processed < self.size):
            if current < self.capacity - 1:
                current += 1
            else:
                current = 0
            txt += ", " + str(self.queue[current])
            processed += 1

        return txt + "]"

    def empty(self):
        return 0 == self.size

    def enqueue(self, data):
        if self.head == None:
            self.head = 0
            self.tail = 0
        else:
            if self.head <= self.tail:
                if self.tail < self.capacity - 1:
                    self.tail += 1
                else:
                    self.tail = 0
                    self.head += 1
            else:
                if self.head < self.capacity - 1:
                    self.head += 1
                    self.tail += 1
                else:
                    self.head = 0
                    self.tail += 1        
       
        if self.size < self.capacity:
            self.size += 1

        self.queue[self.tail] = data

    def dequeue(self):
        if self.head == None:
            return None

        data = self.queue[self.head]
        self.queue[self.head] = 0
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if self.head < self.capacity - 1:
                self.head += 1
            else:
                self.head = 0

        self.size -= 1
        return data

    def search(self, data):
        if self.empty():
            return False

        current = self.head
        processed = 0
        while(processed < self.size):
            if data == self.queue[current]:
                return True
            if current < self.capacity - 1:
                current += 1
            else:
                current = 0
            processed += 1

        return False

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

print("\nTesting circular queue (based on a list)")
cql = CircularQueueL(3)
cql.enqueue(5)
cql.enqueue(2)
cql.enqueue(3)
print("Added some data (full capacity): " + str(cql))

cql.enqueue(7)
cql.enqueue(1)
print("Added more data: " + str(cql))
print("Queue size: " + str(len(cql)))

print("Look for 7: " + str(cql.search(7)))
print("Look for 3: " + str(cql.search(3)))
print("Look for 1: " + str(cql.search(1)))
print("Look for 9: " + str(cql.search(9)))

cql.dequeue()
print("Removed an element: " + str(cql))
print("Queue size: " + str(len(cql)))

cql.dequeue()
print("Removed an element: " + str(cql))
print("Queue size: " + str(len(cql)))

cql.dequeue()
print("Removed an element: " + str(cql))
print("Queue size: " + str(len(cql)))

print("\nTesting circular queue (based on an array)")
cqa = CircularQueueA(3)
cqa.enqueue(5)
cqa.enqueue(2)
cqa.enqueue(3)
print("Added some data (full capacity): " + str(cqa))

cqa.enqueue(7)
print("Added some data (full capacity): " + str(cqa))

print("Searching for 7: " + str(cqa.search(7)))
print("Searching for 2: " + str(cqa.search(2)))
print("Searching for 5: " + str(cqa.search(5)))

cqa.dequeue()
print("Removed some data: " + str(cqa))

cqa.dequeue()
print("Removed some data: " + str(cqa))

cqa.dequeue()
print("Removed some data: " + str(cqa))