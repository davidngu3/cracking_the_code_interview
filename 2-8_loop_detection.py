class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
        self.traversed = False # add this attribute to detect loop

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

def detectLoop(list1):
    node = list1.head

    while node:
        # mark current node as traversed; if already traversed, then that is the intersecting node
        if node.traversed:
            return node
        else:
            node.traversed = True
        
        # traverse both nodes
        if node.next:
            node = node.next

    return None

if __name__ == "__main__":
    list1 = LinkedList()
    tail = list1.addNode(3)
    list1.addNode(4)
    loophead = list1.addNode(5)
    list1.addNode(6)
    list1.addNode(7)

    tail.next = loophead

    print(detectLoop(list1).data)

    
