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
    # capacity is 3
    def __init__(self):
        self.stacks = [Stack()]
        self.sizes = [0]

    def push(self, data):
        self.stacks[-1].push(data)
        self.sizes[-1] += 1
        if self.sizes[-1] >= 3:
            self.stacks.append(Stack())
            self.sizes.append(0)

    def pop(self, stack):
        if self.sizes[stack] > 0:
            self.stacks[stack].pop()
            self.sizes[stack] -= 1

    def printStacks(self):
        for stack in self.stacks:
            stack.print()
        print("newstackset----")
        


if __name__ == "__main__":
    plates = StackSet()
    plates.push(1)
    plates.push(4)
    plates.push(3)
    plates.push(2)
    plates.push(6)
    plates.push(9)  
    plates.push(2)
    plates.push(1)
    plates.push(5)
    plates.push(2)
    plates.printStacks()
    plates.pop(0)
    plates.pop(0)
    plates.pop(1)
    plates.printStacks()
