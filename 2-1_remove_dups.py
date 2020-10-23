# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

import unittest

## LINKED LIST DATA STRUCTURE
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.seen = []

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        print(" ")
    
    def deleteNode(self, start, target):
        node = start
        
        # if deleting head
        if node:
            if node.data == target:
                self.head = node.next
                return

        while node:
            if node.next and node.next.data == target:
                node.next = node.next.next
            node = node.next
    
    def addNode(self, val):
        self.head = Node(val, self.head)

    def removeDups(self):
        node = self.head
        self.seen.append(node.data)

        while node.next:
            if node.next.data in self.seen:
                node.next = node.next.next
            node = node.next
            self.seen.append(node.data)



## 

if __name__ == "__main__":
    newNode = Node(2, None)
    newList = LinkedList(newNode)

    newList.addNode(9)
    newList.addNode(9)
    newList.addNode(4)
    newList.addNode(3)
    newList.addNode(4)
    newList.addNode(6)

    newList.printList()
    newList.removeDups()
    newList.printList()






    
    
    
    



