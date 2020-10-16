# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: #51, #100

import unittest

def rotate_matrix(image):
    # max dimension of matrix
    N = len(image)

    # empty matrix for return
    ret = [[[0 for x in range(4)] for j in range(N)] for i in range(N)]

    # rotate each pixel in the image by 90 degrees by swapping the 4 bits
    for r in range(N):
        for c in range(N):
            rotate_pixel(image[r][c])

    # rotate the image 
    for r in range(N):
        for c in range(N):
            ret[r][c] = image[N-1-c][r]

    return ret

def rotate_pixel(pixel):
    pixel[0], pixel[1] = pixel[1], pixel[0]
    pixel[0], pixel[3] = pixel[3], pixel[0]
    pixel[0], pixel[2] = pixel[2], pixel[0]


class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rotate_matrix([[[64, 93, 120, 2], [34, 91, 101, 56]], [[31, 45, 93, 23], [45, 64, 31, 14]]]), 
                        [[[93, 31, 23, 45],[120, 64, 2, 93]],[[31, 45, 14, 64],[101, 34, 56, 91]]])

if __name__ == '__main__':
    unittest.main()
