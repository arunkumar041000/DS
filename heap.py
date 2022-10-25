class Heap:
    def __init__(self) -> None:
        self.array = []

    def __str__(self) -> str:
        return " ".join([str(x) for x in self.array])

    def heapify(self, n, i) -> None:
        arr = self.array
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(n, largest)

    def insert(self, newNum) -> None:
        size = len(self.array)
        if size == 0:
            self.array.append(newNum)
        else:
            self.array.append(newNum)
            for i in range((size//2)-1, -1, -1):
                self.heapify(size, i)

    def deleteNode(self, num) -> None:
        size = len(self.array)
        i = 0
        for i in range(0, size):
            if num == self.array[i]:
                break
        self.array[i], self.array[size-1] = self.array[size-1], self.array[i]
        self.array.remove(num)

        for i in range((len(self.array)//2)-1, -1, -1):
            self.heapify(len(self.array), i)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(3)
    heap.insert(4)
    heap.insert(9)
    heap.insert(5)
    heap.insert(2)

    print("Max-Heap array: " + str(heap))

    heap.deleteNode(4)
    print("After deleting an element: " + str(heap))
