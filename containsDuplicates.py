# Given an array of intergers
# Find if the array contains any duplicates
# Fxn should return Truw if any values appear twice in the array
# Should return False if no duplicates are found

# nums ==> a list of integers
# create an empty set as we loop through the list
# loop through nums and add to dups
# if i is in dups return true
# else if no dups found, return false


class Solution:
    def containsDuplicate(self, nums):
        dups = set()
        for i in nums:
            if i in dups:
                return True
            dups.add(i)

        return False


# 217. Contains Duplicate
# Easy

# 976

# 757

# Add to List

# Share
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1, 2, 3, 1]
# Output: true
# Example 2:

# Input: [1, 2, 3, 4]
# Output: false
# Example 3:

# Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
