# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


#IDEA:
# - Rotate each layer starting from the outside working in

import unittest

def rotate_matrix(image):
    # max dimension of matrix
    N = len(image)

    firstLayer = 0
    lastLayer = N // 2 

    for layer in range(firstLayer, lastLayer):
        # rotate layer
        for i in range(layer, N-1-layer):
            # temp <- top
            temp = image[layer][i]

            # top <- left
            image[layer][i] = image[N-1-i][layer]

            # left <- bottom
            image[N-1-i][layer] = image[N-1-layer][N-1-i]

            # bottom <- right 
            image[N-1-layer][N-1-i] = image[i][N-1-layer]

            # right <- temp
            image[i][N-1-layer] = temp

    return image



class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rotate_matrix([[64, 93, 120, 2], [34, 91, 101, 56], [31, 45, 93, 23], [45, 64, 31, 14]]), 
                        [[45, 31, 34, 64], [64, 45, 91, 93], [31, 93, 101, 120], [14, 23, 56, 2]])

    def test_2(self):
        self.assertEqual(rotate_matrix([[5, 2, 1, 5, 7], [2, 5, 3, 1, 8], [6, 2, 3, 6, 8], [9, 9, 5, 4, 3], [6, 3, 2, 6, 8]]),
                        [[6, 9, 6, 2, 5], [3, 9, 2, 5, 2], [2, 5, 3, 3, 1], [6, 4, 6, 1, 5], [8, 3, 8, 8, 7]])

    def test_3(self):
        self.assertEqual(rotate_matrix([]),[])

    def test_4(self):
        self.assertEqual(rotate_matrix([9]),[9])

if __name__ == '__main__':
    unittest.main()
