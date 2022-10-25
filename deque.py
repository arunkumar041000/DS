class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self) -> int:
        return self.size() == 0

    def addRear(self, item) -> None:
        self.items.append(item)

    def addFront(self, item) -> None:
        self.items.insert(0, item)

    def removeFront(self) -> any:
        return self.items.pop(0)

    def removeRear(self) -> any:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    obj = Deque()
    print(obj.isEmpty())
    obj.addRear(8)
    obj.addRear(5)
    obj.addFront(7)
    obj.addFront(10)
    print(obj.size())
    print(obj.isEmpty())
    obj.addRear(11)
    print(obj.removeRear())
    print(obj.removeFront())
    obj.addFront(55)
    obj.addRear(45)
    print(obj.items)
