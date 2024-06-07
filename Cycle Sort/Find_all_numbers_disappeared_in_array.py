# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        n = len(nums)
        ans = []
        while index < n:

            correct_index = nums[index] - 1

            if nums[index] != nums[correct_index]:
                nums[index], nums[correct_index] = nums[correct_index],  nums[index]
            else:
                index += 1
        
        for index in range(n):
            if index +1 != nums[index]:
                ans.append(index+1)
        
        return ans
