# Given an array of integers nums, sorted in acending order, and a target integer
# nums rotated on a pivot unkn
# searc for the target in nums. if found, return the index,
# else return -1 if not found

# loops over nums
# if i == target, return the index of i
# else return -1


# class Solution:
#     def search(self, nums, target):
#         length = len(nums)
#         for n in range(length):
#             if target not in nums:
#                 return -1
#             elif n == target:
#                 return nums[n]
#             else:
#                 return -1
# not passing test case of [1] target 1


class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1
# passed all test cases
