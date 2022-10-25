
class Node:
    def __init__(self, val) -> None:
        self.left: Node = None
        self.right: Node = None
        self.val = val

    def traversePreOrder(self) -> None:
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self) -> None:
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self) -> None:
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

    def printTree(self, curRoot, indent, last) -> None:
        if curRoot != None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            print(curRoot.val)
            self.printTree(curRoot.left, indent, False)
            self.printTree(curRoot.right, indent, True)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    #                    root(1)
    #                   /      \
    #             left(2)       right(3)
    #            /              /      \
    #      left(4)         left(5)      right(6)

    print("Pre order Traversal: ", end="")
    root.traversePreOrder()
    print("\nIn order Traversal: ", end="")
    root.traverseInOrder()
    print("\nPost order Traversal: ", end="")
    root.traversePostOrder()
    print()
    # root.printTree(root,"",True)
