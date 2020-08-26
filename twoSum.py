# given an array of integers
# return the indices of the 2 numbers that when added together == target


# init list to hold indicies of nums that == target when added together
# loop over nums
# init j as i + 1
# while j is less than the length of nums
# if nums[j] is equal to target - nums[i]
# add i and j (index) to the indices list
# else increment j by 1
# indices=[]
# length= len(nums)
# for i in range(length):
# j=i+1
# while j<length:
# if(nums[j]==target-nums[i]):
# solution.append(j)
# solution.append(i)
# return solution
# else:
# j+=1


class Solution:
    def twoSum(self, nums, target):
        indices = []
        length = len(nums)

        for i in range(length):
            j = i+1
            while j < length:
                if(nums[j] == target-nums[i]):
                    indices.append(i)
                    indices.append(j)
                    return indices
                else:
                    j += 1
# given an array of integers
# return the indices of the 2 numbers that when added together == target


# init list to hold indicies of nums that == target when added together
# loop over nums
   # init j as i + 1
    # while j is less than the length of nums
       # if nums[j] is equal to target - nums[i]
        # add i and j (index) to the indices list
        # else increment j by 1
# indices=[]
# length= len(nums)
# for i in range(length):
    # j=i+1
    # while j<length:
        # if(nums[j]==target-nums[i]):
            # solution.append(j)
            # solution.append(i)
             # return solution
            # else:
                # j+=1


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices = []
#         length = len(nums)

#         for i in range(length):
#             j = i+1
#             while j < length:
#                 if(nums[j] == target-nums[i]):
#                     indices.append(i)
#                     indices.append(j)
#                     return indices
#                 else:
#                     j+=1
# class Solution:
#     def twoSum(self, nums, target):
#         index=[]
#         for f_index, i in enumerate(nums):
#             for s_index, j in enumerate(nums[f_index + 1:]):
#                 if i + j == target:
#                     index.append(f_index)
#                     index.append(f_index + s_index + 1)
#                     return index

class Solution(object):
    def twoSum(self, nums, target):
        cache = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            print('nums[i]', nums[i])
            print('complement', complement)
            if complement not in cache:
                # add to dictionary
                cache[nums[i]] = i
            else:
                return [cache[complement], i]
