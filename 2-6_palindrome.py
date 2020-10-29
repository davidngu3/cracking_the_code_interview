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

    
def reverseList(linkedList):
    node = linkedList.head

    reversedList = LinkedList()

    while node:
        reversedList.addNode(node.data)
        node = node.next

    return reversedList

def checkPalindrome(linkedList):
    node1 = linkedList.head
    
    reversedList = reverseList(linkedList)
    node2 = reversedList.head

    while node1:
        if node1.data is not node2.data:
            return False
        node1 = node1.next
        node2 = node2.next

    return True

if __name__ == "__main__":
    list1 = LinkedList()
    list1.addNode(4)
    list1.addNode(6)
    list1.addNode(2)
    list1.addNode(6)
    list1.addNode(4)

    list2 = LinkedList()
    list2.addNode(2)
    list2.addNode(9)
    list2.addNode(5)

    list3 = LinkedList()
    list3.addNode(4)
    list3.addNode(6)
    list3.addNode(6)
    list3.addNode(4)

    print(checkPalindrome(list1))
    print(checkPalindrome(list2))
    print(checkPalindrome(list3))
