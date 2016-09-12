# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 19:50:48 2016

@author: LeonWen
"""

# LeetCode 001 Two Sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            tempVal = target - nums[i]
            for j in range(i+1,len(nums)):
                if tempVal == nums[j]:
                    x = i
                    y = j
                    return x,y
        
        # return i,j
        
test = Solution()
a,b = test.twoSum([3,2,4],6)
print a,b