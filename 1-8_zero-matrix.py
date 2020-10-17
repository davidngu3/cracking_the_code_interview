# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.

import unittest

def zero_matrix(matrix):
    zero_rows = set()
    zero_cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i in zero_rows) or (j in zero_cols):
                matrix[i][j] = 0
    
    return matrix
    

class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(zero_matrix([[4, 0, 2], [5, 6, 0], [9, 8, 3]]), [[0, 0, 0], [0, 0, 0], [9, 0, 0]])
    
    def test_2(self):
        self.assertEqual(zero_matrix([[3, 2], [0, 1]]), [[0, 2], [0, 0]])

if __name__ == '__main__':
    unittest.main()
