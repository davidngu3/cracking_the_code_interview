class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        print(" ")
    
    def addNode(self, val):
        self.head = Node(val, self.head)
        return self.head

    def partition(self, p):
        node = self.head.next
        prev = self.head

        while node:
            if node.data < p:
                self.addNode(node.data)
                prev.next = node.next
            else:
                prev = node
            node = node.next


if __name__ == "__main__":
    newList = LinkedList()
    newList.addNode(1)
    newList.addNode(2)
    newList.addNode(10)
    newList.addNode(5)
    newList.addNode(8)
    newList.addNode(5)
    newList.addNode(3)

    # newList.printList()
    newList.partition(5)
    newList.printList()
    
