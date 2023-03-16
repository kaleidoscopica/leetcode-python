### 2441. Largest Positive Integer That Exists With Its Negative
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_nums = [x for x in nums if x > 0]
        neg_nums = [x for x in nums if x < 0]
        
        pos_nums.sort()
        pos_nums.reverse()
        neg_nums.sort()

        while len(pos_nums) >= 1 and len(neg_nums) >= 1 and pos_nums[0] != abs(neg_nums[0]):
            if pos_nums[0] > abs(neg_nums[0]):
                del pos_nums[0]
            elif pos_nums[0] < abs(neg_nums[0]):
                del neg_nums[0]

        if len(pos_nums) >= 1 and len(neg_nums) >= 1:
            return pos_nums[0]
        else:
            return -1
