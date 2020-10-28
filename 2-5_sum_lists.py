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
        if not node2:
            ans.next = Node(node1.data)
            ans = ans.next
            node1 = node1.next
        
        elif not node1:
            ans.next = Node(node2.data)
            ans = ans.next
            node2 = node2.next

        else:
            result = node1.data + node2.data + carry
            carry = 0

            if result > 10:
                ans.next = Node(result - 10)
                carry = 1
            else:
                ans.next = Node(result)

            ans = ans.next
            node1 = node1.next
            node2 = node2.next
    
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
    
