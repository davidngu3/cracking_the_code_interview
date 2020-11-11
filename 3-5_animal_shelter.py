class QueueNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def enqueue(self, val):
        newNode = QueueNode(val)
        if self.back:
            self.back.next = newNode
        self.back = newNode
        # if only one node in queue, it is both front and back
        if self.front == None:
            self.front = self.back
        return self.back

    def dequeue(self, val):
        returnItem = self.front
        self.front = self.front.next

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        print(" ")


if __name__ == "__main__":
    

    
