class Array:
    """
    A sample implementation of array data structure. For a simplicity
    there is no type enforcing.

    Attributes
    ----------
    size : int
        size of array, must be greater than 0

    array : list
        array

    Methods
    -------
    set(index, value)
        Stores value at index

    get(index=None)
        Returns value stored at index or the whole array if index=None
    """
    def __init__(self, size):
        if size < 1:
            raise ValueError("Array size must be greater than 0")

        self.size = size
        self.array = [0] * size

    def __str__(self):
        txt = "["

        for item in self.array:
            txt += str(item) + ", "

        return txt[:-2] + "]"

    def set(self, index, value):
        if (index < 0) or index > self.size - 1:
            raise ValueError("Index out of bound. Array length is " + str(self.size))

        self.array[index] = value

    def get(self, index=None):
        if index == None:
            return self.array

        if (index < 0) or index > self.size - 1:
            raise ValueError("Index out of bound. Array length is " + str(self.size))

        return self.array[index]

class DynamicArray:
    """
    A sample implementation of dynamic array data structure.
    For a simplicity there is no type enforcing.

    Attributes
    ----------
    size : int
        number of elements in the array

    capacity : int
        available capacity

    array : list
        dynamic array

    Methods
    -------
    get(index)
        Gets value stored at index.

    insert(value, index)
        Inserts value at index. Dynamically adjusts the capacity if
        the maximum one was reached.

    remove(index)
        Removes value at index and shifts back any following values.
    """
    def __init__(self, capacity=1):
        if capacity < 1:
            raise ValueError("Array capacity must be greater than 0")
        self.size = 0
        self.capacity = 2 * capacity
        self.array = self.__initArray(self.capacity)

    def __len__(self):
        return self.size

    def __str__(self):
        txt = "["

        for i in range(self.size):
            txt += str(self.array[i]) + ", "

        return txt[:-2] + "]"

    def __initArray(self, capacity):
        return [0] * capacity

    def __grow(self):
        origCapacity = self.capacity
        origArr = self.array

        self.capacity = 2 * self.capacity
        self.array = self.__initArray(self.capacity)

        for i in range(origCapacity):
            self.array[i] = origArr[i]

    def get(self, index):
        if (index < 0) or index > self.size - 1:
            raise ValueError("Index out of bound. Array length is " + str(self.size))

        return self.array[index]


    def insert(self, value, index):
        if (index < 0) or index > self.size:
            raise ValueError("Index out of bound. Array length is " + str(self.size))

        if self.size == self.capacity:
            self.__grow()

        if index < self.size:
            for i in range(self.size, index - 1, -1):
                self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.size += 1

    def remove(self, index):
        if (index < 0) or index > self.size - 1:
            raise ValueError("Index out of bound. Array length is " + str(self.size))

        for i in range(index + 1, self.size):
            self.array[i - 1] = self.array[i]

        self.size -= 1
        self.array[self.size] = 0


print("Array class testing")
arr = Array(5)
arr.set(2, 12)
arr.set(1, 5)

print("Cast to string: " + str(arr))
print("Get value at index=2: " + str(arr.get(2)))

print("\n\nDynamic array testing")
darr = DynamicArray()
darr.insert(1, 0)
darr.insert(3, 1)
darr.insert(5, 2)
darr.insert(7, 3)
print("Added some values: " + str(darr))
print("Capacity = " + str(darr.capacity) + ", size = " + str(len(darr)))

darr.remove(0)
print("\nRemove the first value: " + str(darr))
print("Capacity = " + str(darr.capacity) + ", size = " + str(len(darr)))

darr.remove(2)
print("\nRemove the last value: " + str(darr))
print("Capacity = " + str(darr.capacity) + ", size = " + str(len(darr)))

darr.insert(1, 1)
darr.insert(8, 3)
darr.insert(9, 0)
print("\nAdded some values: " + str(darr))
print("Capacity = " + str(darr.capacity) + ", size = " + str(len(darr)))
