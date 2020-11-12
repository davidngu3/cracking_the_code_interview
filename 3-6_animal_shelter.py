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

    def dequeueAny(self):
        returnItem = self.front
        self.front = self.front.next

    def dequeueCat(self):
        # if no cat pointer yet
        returnItem

    def dequeueDog(self):
        return True

    def print(self):
        node = self.front
        while node:
            print(node.data)
            node = node.next
        print(" ")


if __name__ == "__main__":
    animals = Queue()
    animals.enqueue('dog')
    animals.enqueue('dog')
    animals.enqueue('cat')
    animals.enqueue('cat')
    animals.enqueue('dog')
    

    animals.print()
    

    
