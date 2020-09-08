class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return if array has 1 element or empty
        # set length of nums to a vairable
        n = len(nums)
        if n == 0 or n == 1:
            return n

        temp = list(range(n))

        # traverse elements
        j = 0
        for i in range(0, n-1):
            # if current element is not equal to the next element then store that current element
            if nums[i] != nums[i + 1]:
                temp[j] = nums[i]
                j += 1
        # store the last element as whether it is unique or repeated, it hasn't been stored previously.
        temp[j] = nums[n-1]
        j += 1
        # modify the original array
        for i in range(0, j):
            nums[i] = temp[i]

        return j
