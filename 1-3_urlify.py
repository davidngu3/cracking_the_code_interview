# 1.3 URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith     "
# Output: "Mr%20John%20Smith"

# IDEA:
# A common approach to string manipulation is iterating in reverse order to get around overwriting pending info

# Note: python strings are immutable, use lists instead
def urlify(string, length):
    new_index = len(string) # end of string

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string
    


if __name__ == "__main__":
    print(urlify(list("Mr John Smith    "), 13))