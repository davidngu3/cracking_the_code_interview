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

    def insert(self, key):
        if not self.root:  # case: no root
            self.root = Node(key)
        else:
            self.rec_insert(self.root, key)

    def rec_insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.rec_insert(root.left, key)
        else:
            root.right = self.rec_insert(root.right, key)
        
        return root
    
def createMinTree(arr):
    # create empty BST
    minBST = BST()

    def recursiveAdd(left, right):
        if right >= left:
            midPoint = left + ((right - left) // 2)

            minBST.insert(arr[midPoint])
            recursiveAdd(left, midPoint - 1)
            recursiveAdd(midPoint + 1, right)
        
        return 0
    
    recursiveAdd(0, len(arr) - 1)
    


# class TestMethods(unittest.TestCase):
#     def test_1(self):

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]

    createMinTree(arr)
    
    # unittest.main() 

