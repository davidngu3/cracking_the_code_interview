# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# IDEAS:
# If able to use additional data structures, I would use a hash table (dictionary in python) because it would allow fast lookup

def isUnique(string): 
    alphabetHash = {}

    # enter each character c into a hashtable, if already entry at c then return false
    for char in string:
        if char in alphabetHash:
            return False
        alphabetHash[char] = 1

    return True

# If not able to use additional data structures, I would first sort the string then check adjacent values for inequality

def isUniqueInPlace(string):
    sortedString = sorted(string)

    for i, c in enumerate(sortedString):
        if i > 0:
            if sortedString[i] == sortedString[i-1]:
                return False

    return True


if __name__ == "__main__":
    print(isUnique("abca"))
    print(isUnique("a"))
    print(isUnique("abcfgh"))
    print(isUnique(""))

    print(isUniqueInPlace("abca"))
    print(isUniqueInPlace("a"))
    print(isUniqueInPlace("abcfgh"))
    print(isUniqueInPlace(""))

    
