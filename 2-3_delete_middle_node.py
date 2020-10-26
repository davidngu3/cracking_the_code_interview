class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head):
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



if __name__ == "__main__":
    newNode = Node(12, None)
    newList = LinkedList(newNode)

    middleNode = newList.addNode(9)
    newList.addNode(5)
    newList.addNode(1)

    newList.printList()
    
    # given just middleNode, how to delete it?
    while middleNode.next:
        if not middleNode.next.next:
            middleNode.next = None
        else:
            middleNode.data = middleNode.next.data
            middleNode = middleNode.next

    newList.printList()
    
