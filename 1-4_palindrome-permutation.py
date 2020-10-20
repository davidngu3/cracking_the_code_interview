# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

# Solutions:
# - A possible and efficient solution (same time comp) is to use a bit vector, and toggle the ith bit for each char
#   - Then, if there's only one or no '1' bit, then return True.
#   - To check if there's only one '1' bit, we can do result & (result - 1) == 0

import unittest

def check_palindrome(string):
    # first standardize string by remove whitespace and lowercase
    standardizedString = string.replace(' ', '').lower()

    # enter characters in hash set
    charHash = {}
    for char in standardizedString:
        if char not in charHash:
            charHash[char] = 0
        charHash[char] += 1

    # count hash entries with odd count
    oddCounts = 0
    for char in charHash:
        if charHash[char] % 2 != 0:
            oddCounts += 1

    # string can be arranged into palindrome if 0 or 1 odd count chars
    return False if oddCounts > 1 else True



class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertFalse(check_palindrome('abbc'))

    def test_2(self):
        self.assertTrue(check_palindrome('baba'))

    def test_3(self):
        self.assertTrue(check_palindrome('rcarace'))

    def test_4(self):
        self.assertTrue(check_palindrome('atco  cta'))
  

if __name__ == '__main__':
    unittest.main()