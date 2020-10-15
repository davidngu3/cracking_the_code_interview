import unittest

def compress_string(string):
    if len(string) == 0:
        return string

    is_compressed = False
    ret = ""
    curr = string[0]
    counter = 1

    for char in string[1:] + "0":
        if curr != char:
            if counter > 1:
                is_compressed = True
            ret += curr + str(counter)
            curr = char
            counter = 1
        else:
            counter += 1

    if not is_compressed:
        return string
    else:
        return ret
  

class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compress_string('aabcccccccaaa'), 'a2b1c7a3')

    def test_2(self):
        self.assertEqual(compress_string('zdsaa'), 'z1d1s1a2')

    def test_uppercase(self):
        self.assertEqual(compress_string('AaabBbEeeE'), 'A1a2b1B1b1E1e2E1')

    def test_original(self):
        self.assertEqual(compress_string('dcbad'), 'dcbad')

    def test_empty(self):
        self.assertEqual(compress_string(''), '')

if __name__ == '__main__':
    unittest.main()
