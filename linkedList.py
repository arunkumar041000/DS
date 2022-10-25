class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def hasNext(self) -> bool:
        return self.head is not None

    def insertAtBeginning(self, new_data) -> None:
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node: Node, new_data) -> None:
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data) -> None:
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def deleteNode(self, position: int) -> None:
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None or temp.next is None:
            return

        next = temp.next.next
        temp.next = next

    def has(self, key) -> bool:
        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    def sortLinkedList(self, head: Node) -> None:
        current = head
        index = Node(None)

        if head is None:
            return
        while current is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data

                index = index.next
            current = current.next

    def printList(self) -> None:
        node = self.head
        res = ""
        while (node):
            res += (str(node.data) + " -> ")
            node = node.next
        print(res[:-3])


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    llist.deleteNode(3)
    print("\nAfter deleting 3 an element:")
    llist.printList()

    print()
    item_to_find = 3
    if llist.has(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()
