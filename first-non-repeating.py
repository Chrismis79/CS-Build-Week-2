# Given a string (s)
# Find and return the first instance of a NON_REPEATING character.
# If no repeating character, return '_'

# EX s = 'abacabad'
# output should be 'c'
# 2 characters are NOT duplicates here, BUT 'c' is THE FIRST

# Planning
# Chara count array to keep track of the # of times a character appears. Hash tbl?
# init hash
# Traverse the string (s) keeping track with a pointer var.
# Incement count by 1 of pointer in hash
# Traverse string and check whether the current chara has > 1 count.
# If the freq is < 1 continue
# else break loop and print the current character.

# Return the first character with a count of 1 + current letter.

# def getCharCount(s):
#     char_count = [0] * 256

#     for c in s:
#         char_count[ord(c)] += 1
#         print('char_count')
#     return char_count


# def first_not_repeating_character(s):
#     count = getCharCount(s)
#     idx = -1
#     j = 0
#     result = ''

#     for c in s:
#         print(c)
#         if count[ord(c)] == 1:
#             result = c
#             j += 1
#         else:
#             return '_'


#     return result

def first_not_repeating_character(s):
    # empty list  to hold characters visited
    char_order = []
    # empty dictionary to hold visited chara and the count of each
    cache = {}
    for c in s:
        # For each character in the string
        if c in cache:
            # if the character is in the cache, increment the count by 1
            cache[c] += 1
        else:
            # else add c to dictionary with value of 1
            cache[c] = 1
            # append character to list (I don't think I need the list)
            char_order.append(c)
    for c in char_order:
        # for character in char_order list, if current count == to 1, return character
        # This passed test cases, but after re looking at my code this should be >1 or ==2 to return the correct result off the platform.
        if cache[c] == 2:
            return c
    # If no repeating character found  return '_'
    return '_'


# Runtime O(n2)
# Improvements: I think I could make the space complexity better by not creating a new list, but tracking the current value and returning the first duplicate character. Then I wouldn't need the second for loop.
