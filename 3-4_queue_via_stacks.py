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
        self.newStack = Stack()
        self.oldStack = Stack()
    
    # push onto newStack
    def push(self, data):
        self.newStack.push(data) 

    # for popping, take top off of oldStack; if empty, transfer newstack to oldstack (in reverse order)
    def pop(self):
        if self.oldStack.top:
            return self.popOld()
        
        while self.newStack.top:
            poppedItem = self.newStack.pop()
            self.oldStack.push(poppedItem.data)
        
        return self.popOld()
    
    def popOld(self):
        poppedItem = self.oldStack.top

        # delete top node
        if self.oldStack.top.next:
            self.oldStack.top = self.oldStack.top.next
        else:
            self.oldStack.top = None
            
        return poppedItem

    def print(self):
        node = self.newStack.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")

        node = self.oldStack.top
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

    print(queue.pop().data)

    queue.print()

    queue.push(5)
    queue.push(13)

    print(queue.pop().data)

    queue.print()