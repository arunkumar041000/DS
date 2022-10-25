class Stack:
    def __init__(self, k: int) -> None:
        self.__stacksize = k  # stack max size
        self.create_stack()

    def __str__(self) -> str:
        return "the Stack : \n\n"+"".join([" ↓| "+str(x)+" |↑\n  +---+ \n" for x in self.__stack])

    def create_stack(self) -> None:
        self.__stack = []

    def clear(self) -> None:
        self.create_stack()

    def size(self) -> int:
        return len(self.__stack)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def push(self, item) -> None:
        if self.size() == self.__stacksize:
            print("can't push {}. The circular queue is full\n".format(item))
            return
        self.__stack.append(item)

    def pop(self) -> any:
        if not self.isEmpty():
            return self.__stack.pop()
        else:
            print("Stack is Empty")


if __name__ == "__main__":
    obj = Stack(5)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(3)
    obj.push(3)

    print("Stack size: {}".format(obj.size()))

    print(obj)
