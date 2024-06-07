# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        n = len(nums)
        ans = []

        while index < n:
            correct_index = nums[index] - 1

            if nums[index] != nums[correct_index]:
                nums[index], nums[correct_index] = nums[correct_index], nums[index]
            else:
                index += 1
        
        for i in range(n):
            if nums[i] != i +1:
                ans.append([nums[i],i+1])
                return [nums[i], i+1]
        
