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

print("Array class testing")
arr = Array(5)
arr.set(2, 12)
arr.set(1, 5)

print("Cast to string: " + str(arr))
print("Get value at index=2: " + str(arr.get(2)))