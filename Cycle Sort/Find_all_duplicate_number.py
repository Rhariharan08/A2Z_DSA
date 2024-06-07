# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        index = 0
        while index < len(nums):

            correct_index = nums[index] - 1

            
            if nums[index] <= len(nums) and nums[index] != nums[correct_index]:
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
            else:
                index += 1
        
        for index in range(len(nums)):
            if nums[index] != index + 1:
                ans.append(nums[index])
        
        return ans
