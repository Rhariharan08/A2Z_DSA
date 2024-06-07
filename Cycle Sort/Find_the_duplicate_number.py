# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        index = 0

        while index < n:
            if nums[index] != index + 1:
                correct_index = nums[index] - 1
                
                if nums[index] != nums[correct_index]:
                    nums[index], nums[correct_index] = nums[correct_index], nums[index]
                else:
                    return nums[index]
            else:
                index += 1
        
        
        
       
