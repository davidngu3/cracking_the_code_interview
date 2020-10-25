class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.seen = {}

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        print(" ")
    
    def addNode(self, val):
        self.head = Node(val, self.head)

    def getKthLast(self, k):
        behind = self.head
        
        # set up the runner
        runner = self.head
        for i in range(k):
            runner = runner.next
        
        # traverse list until runner hits end
        while runner:
            runner = runner.next
            behind = behind.next
        
        return behind.data



if __name__ == "__main__":
    newNode = Node(2, None)
    newList = LinkedList(newNode)

    newList.addNode(5)
    newList.addNode(4)
    newList.addNode(6)
    newList.addNode(7)
    newList.addNode(1)
    newList.addNode(9)

    newList.printList()
    print(newList.getKthLast(7))