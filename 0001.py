### 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate through the nums array twice. i and j are the indices corresponding to each loop,
        # and num and num2 are their respective values found during each loop.
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                # If the number at index i plus the number at index j equal the target, and i is not the same as j,
                if nums[i] + nums[j] == target and i!=j:
                    # Then return the two indices
                    return [i, j];
