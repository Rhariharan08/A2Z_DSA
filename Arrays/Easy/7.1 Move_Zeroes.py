#Problem Link -> https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        
				s = [0] * len(nums)
				j=0
				for i in range(len(nums)):
					if nums[i] != 0:
						s[j] = nums[i]
						j+=1
				for i in range(len(nums)):
					nums[i] = s[i]
        
