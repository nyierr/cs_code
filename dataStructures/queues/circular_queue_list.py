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

print("Testing circular queue")
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