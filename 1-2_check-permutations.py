# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# IDEAS:
# Sort both and check equality: O(Alog(A) + Blog(B))
# Bitmap of characters: O(A + B)
# Hashset: O(A + B)

def checkPermutations(string1, string2): 
    charHash = {}
    
    # optimisation: permutations must be same length
    if len(string1) != len(string2):
        return False
    
    # increment chars from string 1 in hash 
    for char in string1:
        if char not in charHash:
            charHash[char] = 0
        charHash[char] += 1

    # decrement chars from string 2 in hash
    for char in string2:
        if char not in charHash:
            return False
        charHash[char] -= 1
    
    # check all hash values cancel out (equal to 0)
    for char in charHash:
        if charHash[char] != 0:
            return False

    return True

def checkPermutationsSort(string1, string2):
    if len(string1) != len(string2):
        return False

    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    # general case
    print(checkPermutations('abdec', 'ecbda'))
    
    # same characters but different frequencies
    print(checkPermutations('aabc', 'ccab'))

    # same length different characters
    print(checkPermutations('aegz', 'eope'))

    # different lengths same characters
    print(checkPermutations('aabc', 'abc'))

    # special characters
    print(checkPermutations('%235@5', '%253@5'))


    print(checkPermutationsSort('abdec', 'ecbda'))
    print(checkPermutationsSort('aabc', 'ccab'))
    print(checkPermutationsSort('aegz', 'eope'))
    print(checkPermutationsSort('aabc', 'abc'))
    print(checkPermutationsSort('%235@5', '%253@5'))
    

    
