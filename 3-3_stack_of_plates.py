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
    
    def print(self):
        node = self.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")

class StackSet:
    def __init__(self, stacks = []):
        self.stacks = stacks

    def printStacks(self):
        print(" ")


if __name__ == "__main__":
    newStack = Stack()
    newStack.push(5)
    newStack.push(7)
    newStack.push(2)
    newStack.push(1)

    newStack.print()

    newStack.pop()
    newStack.print()
    
