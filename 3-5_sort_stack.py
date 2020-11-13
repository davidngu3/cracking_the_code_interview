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

        return None
    
    def peek(self):
        if self.top:
            return self.top.data

        return False

    def print(self):
        node = self.top
        while node:
            print(node.data, end="-")
            node = node.next
        print("\n")

    def isEmpty(self):
        if self.top:
            return False
        return True

def sortStack(s):
    r = Stack()
    
    while not s.isEmpty():
        popped = s.pop() # temporarily store current node
        # iterate tempstack to find correct position, while popping and storing temporarily in original stack
        while (not r.isEmpty()) and (r.peek() > popped.data):
            s.push(r.pop().data)
        r.push(popped.data)

    # copy from r back into s, making original stack ascending order
    while not r.isEmpty():
        s.push(r.pop().data)
    
    return True


if __name__ == "__main__":
    newStack = Stack()
    newStack.push(5)
    newStack.push(8)
    newStack.push(2)
    newStack.push(3)
    newStack.print()

    sortStack(newStack)

    newStack.print()
