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

print("Testing circular queue")
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