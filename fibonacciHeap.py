import math
from typing import List


def floor_log(x) -> int:
    return math.frexp(x)[1] - 1


class FibonacciTree:
    def __init__(self, value) -> None:
        self.value = value
        self.child = []
        self.order: int = 0

    def add_at_end(self, t) -> None:
        self.child.append(t)
        self.order = self.order + 1


class FibonacciHeap:
    def __init__(self) -> None:
        self.trees: List[FibonacciTree] = []
        self.least: FibonacciTree = None
        self.count = 0

    def insert_node(self, value) -> None:
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self) -> any:
        if self.least is None:
            return None
        return self.least.value

    def extract_min(self) -> any:
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.value

    def consolidate(self) -> None:
        aux: List[FibonacciTree] = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.least.value):
                    self.least = k


if __name__ == "__main__":
    heap = FibonacciHeap()

    heap.insert_node(7)
    heap.insert_node(3)
    heap.insert_node(17)
    heap.insert_node(24)

    print('the minimum value of the fibonacci heap: {}'.format(heap.get_min()))

    print('the minimum value removed: {}'.format(heap.extract_min()))
