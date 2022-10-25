class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return " ".join([str(x) for x in self.queue])

    def heapify(self, n, i) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.queue[i] < self.queue[l]:
            largest = l

        if r < n and self.queue[largest] < self.queue[r]:
            largest = r

        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.heapify(n, largest)

    def insert(self, item) -> None:
        size = len(self.queue)
        if size == 0:
            self.queue.append(item)
        else:
            self.queue.append(item)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    def delete(self, item) -> None:
        size = len(self.queue)
        i = 0
        for i in range(0, size):
            if item == self.queue[i]:
                break

        self.queue[i], self.queue[size -
                                  1] = self.queue[size - 1], self.queue[i]
        self.queue.remove(size - 1)

        for i in range((len(self.queue) // 2) - 1, -1, -1):
            self.heapify(len(self.queue), i)


if __name__ == "__main__":
    obj = Queue()

    obj.insert(3)
    obj.insert(4)
    obj.insert(9)
    obj.insert(5)
    obj.insert(2)

    print("Max-Heap array: " + str(obj))

    obj.delete(4)
    print("After deleting an element: " + str(obj))
