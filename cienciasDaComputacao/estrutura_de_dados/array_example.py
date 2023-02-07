import sys


class ListaArray:
    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        return self.data.pop(index)

    def update(self, index, value):
        self.data[index] = value


array = ListaArray()

array.set(0, "Felipe")
array.set(1, "Ana")

array_memory_size = sys.getsizeof(array.data)
# print(array_memory_size)

array.set(2, "Shirley")
array.set(3, "Miguel")

array_memory_size = sys.getsizeof(array.data)
# print(array_memory_size)

array.set(4, "Alberto")
array.set(5, "Marta")
array.set(6, "Túlio")
array.set(7, "Michelle")

array_memory_size = sys.getsizeof(array.data)
# print(array_memory_size)

array.update(6, "Guilherme")
# print(array)


index = 0

while index < len(array):
    # print("Index:", index, ", Nome:", array.get(index))
    index += 1
