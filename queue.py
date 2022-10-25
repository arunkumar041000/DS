

class Queue:
    def __init__(self, k: int) -> None:
        self.queuesize = k # queue max size
        self.queue = []

    def __str__(self) -> str:
        return " <- ".join([str(x) for x in self.queue if x])

    def enqueue(self, item) -> None:
        if self.size() == self.queuesize:
            print("can't enqueue {}. The circular queue is full\n".format(item))
            return
        self.queue.append(item)

    def dequeue(self) -> any:
        if self.size() < 1:
            print("The circular queue is empty\n")
            return
        return self.queue.pop(0)

    def size(self) -> int:
        return len([x for x in self.queue if x])


if __name__ == "__main__":
    obj = Queue(5)

    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)

    print("Stack size: {}".format(obj.size()))
    obj.dequeue()

    print(obj)
