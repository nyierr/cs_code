class Node:
    """
    A sample implementation of a singly linked list node.

    Attributes
    ----------
    data : 
        data stored in a node

    next_node : Node
        next node

    Methods
    -------
    get_next()
        Returns the next node

    set_next(Node)
        Sets the next node to Node

    get_data()
        Returns the data stored in the node

    set_data(data)
        Sets the data stored in the node to data
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class SList:
    """
    A sample implementation of a singly linked list.

    Attributes
    ----------
    head : Node
        head (first element) of list

    tail: Node
        tail (last element) of list

    size : int
        size of list (number of nodes)

    Methods
    -------
    empty()
        Returns True if list is empty; False otherwise.

    append(data)
        Appends a new node containing data to the list.

    insert(data, index)
        Inserts a new node containing data at position index.

    remove(index)
        Removes a node at position index and returns its data.

    index(data)
        Returns the index of the first node that stores data.
        If no matching node found, returns -1.

    update(data, index)
        Updates data stored by the node at position index.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):     
        if self.head == None:
            return "[]"

        current = self.head
        txt = "[" + str(current.get_data())

        while(current.get_next()):
            current = current.get_next()
            txt += ", " + str(current.get_data())

        return txt + "]"

    def __find(self, index):
        current = self.head

        position = 0
        while(position < index):
            current = current.get_next()
            position += 1      
        
        return current

    def empty(self):
        return 0 == self.size

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

        self.size += 1

    def insert(self, data, index):
        if (index < 0) or index > self.size:
            raise ValueError("Index out of bound. List size is " + str(self.size))

        if index == 0:
            self.head = Node(data, self.head)
            if self.tail == None:
                self.tail = self.head
        elif index == self.size:
            self.tail.set_next(Node(data))
            self.tail = self.tail.get_next()
        else:
            current = self.__find(index - 1)
            new_node = Node(data, current.get_next())
            current.set_next(new_node)

        self.size += 1

    def remove(self, index):
        if (index < 0) or index > self.size:
            raise ValueError("Index out of bound. List size is " + str(self.size)) 

        current = self.head
        self.size -= 1

        if index == 0:
            if self.tail == self.head:
                self.tail = None
            self.head = current.get_next()
            return current.get_data()

        current = self.__find(index - 1)
        removed = current.get_next()
        current.set_next(removed.get_next())

        if self.tail == removed:
            self.tail = current

        return removed.get_data()

    def index(self, data):
        position = 0

        current = self.head
        while(current.get_next()):
            if data == current.get_data():
                return position
            current = current.get_next()
            position += 1

        return position if data == current.get_data() else -1

    def update(self, data, index):
        if (index < 0) or index > self.size:
            raise ValueError("Index out of bound. List size is " + str(self.size))

        if index == self.size - 1:
            self.tail.set_data(data)
        else:
            self.__find(index).set_data(data)

print("Testing SList")
slist = SList()

slist.append(5)
slist.append(3)
slist.append(7)
print("After appeneding three values: " + str(slist))

slist.insert(2, 0)
print("After inserting 2 at index 0 (first): " + str(slist))

slist.insert(1, 4)
print("After inserting 1 at index 4 (last): " + str(slist))

slist.insert(4, 3)
print("After inserting 4 at index 3 (middle): " + str(slist))

print("List size: " + str(len(slist)))

slist.remove(0)
print("After removing the first element: " + str(slist))
print("List size: " + str(len(slist)))

slist.remove(4)
print("After removing the last element: " + str(slist))
print("List size: " + str(len(slist)))

slist.remove(1)
print("After removing a middle element: " + str(slist))
print("List size: " + str(len(slist)))

print("5 is at index: " + str(slist.index(5)))
print("7 is at index: " + str(slist.index(7)))
print("8 is at index: " + str(slist.index(8)))

slist.update(50, 0)
print("After updating the first element: " + str(slist))

slist.update(70, 2)
print("After updating the last element: " + str(slist))