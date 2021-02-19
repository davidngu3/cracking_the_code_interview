import unittest
# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.
# Hints: #19, #73, #176

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root = None):
        self.root = root

    def insert(self, node, head = None):
        if not self.root:  # case: no root
            self.root = node

        else:
            if not head:
                head = self.root

            if node.val < head.val:
                if not head.left:
                    head.left = node
                else:
                    self.insert(node, head.left)
            else:
                if not head.right:
                    head.right = node
                else:
                    self.insert(node, head.right)
                
            

# class TestMethods(unittest.TestCase):
#     def test_1(self):

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]

    midPoint = (len(arr) - 1) // 2 

    aBST = BST()

    newNode = Node(5)
    aBST.insert(newNode)
    newNode = Node(3)
    aBST.insert(newNode)
    newNode = Node(15)
    aBST.insert(newNode)
    newNode = Node(34)
    aBST.insert(newNode)

    print(aBST.root.val)
    print(aBST.root.left.val)
    print(aBST.root.right.val)
    print(aBST.root.right.right.val)
    
    # unittest.main() 

