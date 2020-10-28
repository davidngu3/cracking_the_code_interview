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

def sumLists(list1, list2):
    ansHead = Node(0)
    ans = ansHead

    node1 = list1.head
    node2 = list2.head
    carry = 0

    while node1 or node2:
        node1Val = node1.data if node1 else 0
        node2Val = node2.data if node2 else 0

        result = node1Val + node2Val + carry
        carry = 0  # reset carry digit

        if result > 10:
            ans.next = Node(result - 10)
            carry = 1
        else:
            ans.next = Node(result)

        if node1: 
            node1 = node1.next
        if node2: 
            node2 = node2.next
        ans = ans.next

    return LinkedList(ansHead.next)



if __name__ == "__main__":
    list1 = LinkedList()
    list1.addNode(6)
    list1.addNode(1)
    list1.addNode(7)
    list1.addNode(3)

    list2 = LinkedList()
    list2.addNode(2)
    list2.addNode(9)
    list2.addNode(5)

    ans = sumLists(list1, list2)
    ans.printList()
    
