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

print("Testing queue")
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