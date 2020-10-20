# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# IDEAS:
# If able to use additional data structures, I would use a hash table (dictionary in python) because it would allow fast lookup

# SOLUTION:
# - Ask interviewer if ASCII (128, or 256 for extended ASCII) or Unicode
# - I used hash initially but could equivalently use an array of length {alphabetSize}
# - If we can't use additional data structures, we could compare each char against eachother O(n^2)
# - OR if we can modify input string, we could sort (in place) and check linearly for neighbors

# TIME COMPLEXITY:
# - O(n), where n is length of string. Alternatively O(1) since n is never > 128
# SPACE COMPLEXITY:
# - O(1), always array of size 128 regardless of n


def isUnique(string): 
    if len(string) > 128: return False

    charSet = [ None for _ in range(128) ]

    # enter each character c into array, if already entry at c then return false
    for i in range(len(string)):
        charCode = ord(string[i])
        if charSet[charCode]:
            return False

        charSet[charCode] = 1

    return True

# If not able to use additional data structures, I would first sort the string then check adjacent values for inequality

def isUniqueInPlace(string):
    string = sorted(string)

    for i, c in enumerate(string):
        if i > 0:
            if string[i] == string[i-1]:
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

    
