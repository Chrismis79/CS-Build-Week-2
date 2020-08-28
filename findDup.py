# Given a list of nums
# containing n + 1 intergers
# each interger is between 1 and n (inclusive)
# prove that at least 1 duplicate exisits
# Assume only 1 duplicate number --> return first duplicate

# loop over nums
# save numbers in cache as iterated over
# If num is in cache, return num


class Solution:
    def findDuplicate(self, nums):
        cache = set()
        for n in nums:
            if n not in cache:
                cache.add(n)

            else:
                return n
