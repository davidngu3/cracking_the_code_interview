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

def checkIntersection(list1, list2):
    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        # mark current node as traversed; if already traversed, then that is the intersecting node
        if node1:
            if node1.traversed:
                return node1.data
            else:
                node1.traversed = True

        if node2:
            if node2.traversed:
                return node2.data
            else:
                node2.traversed = True
        
        # traverse both nodes
        if node1.next:
            node1 = node1.next
        if node2.next:
            node2 = node2.next
    
    return None

if __name__ == "__main__":
    list1 = LinkedList()
    list1.addNode(3)
    list1.addNode(6)
    intNode = list1.addNode(4)
    list1.addNode(7)
    list1.addNode(9)

    list2 = LinkedList()
    list2.addNode(2)
    list2.head.next = intNode
    list2.addNode(8)

    print(checkIntersection(list1, list2))

    
