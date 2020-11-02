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

    def detectLoop(self):
        slow = self.head
        fast = self.head

        # slow moves p, fast moves 2p
        # once slow enters loop after k nodes, fast has moved 2k nodes, (k % loopsize) nodes into loop
        # fast will catch up to slow after loopsize - (k % loopsize) => collision
        collision = False
        while not collision:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                collision = True

        # at this point, the collision node is K nodes away from start of loop, which is also k nodes away from start of loop
        # the head of the linked list is also k nodes from start of loop
        # traverse both until collision, this is the start of loop
        head = self.head
        loop_found = False
        
        while not loop_found:
            slow = slow.next
            head = head.next
            if slow == head:
                loop_found = True

        return slow

if __name__ == "__main__":
    list1 = LinkedList()
    tail = list1.addNode(3)
    list1.addNode(4)
    loophead = list1.addNode(5)
    list1.addNode(6)
    list1.addNode(7)

    tail.next = loophead

    print(list1.detectLoop().data)

    
