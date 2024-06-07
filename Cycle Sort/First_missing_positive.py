# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        index = 0

        while index < n:

            correct_index = nums[index] - 1

            if nums[index] > 0 and nums[index] <= n and nums[index] != nums[correct_index]:
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
            else:
                index += 1
        
        for index in range(n):
            if nums[index] != index+1:
                return index+1
            
        return n+1
