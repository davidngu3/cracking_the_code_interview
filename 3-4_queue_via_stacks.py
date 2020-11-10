class StackNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self, top=None):
        self.top = top
    
    def push(self, data):
        newNode = StackNode(data)
        if self.top:
            newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top:
            topNode = self.top
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return topNode

        return False
    
    def printStack(self):
        node = self.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")
    

class MyQueue:
    def __init__(self, top=None):
        self.stack = Stack()
        self.tempStack = Stack()
    
    # pushing is normal
    def push(self, data):
        self.stack.push(data) 

    # for popping, we need to pop all nodes, storing them in temp stack, take the top node off then put everything back O(N)
    def pop(self):
        while self.stack.top:
            poppedItem = self.stack.pop()
            self.tempStack.push(poppedItem.data)
        
        returnItem = self.tempStack.top
        self.tempStack.top = self.tempStack.top.next

        while self.tempStack.top:
            poppedItem = self.tempStack.pop()
            self.stack.push(poppedItem.data)
        
        return returnItem
        
    def print(self):
        node = self.stack.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")

        node = self.tempStack.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(3)
    queue.push(4)
    queue.push(2)
    queue.push(5)
    queue.push(6)
    
    queue.print()

    queue.pop()

    queue.print()

    queue.push(5)
    queue.push(13)

    queue.pop()

    queue.print()