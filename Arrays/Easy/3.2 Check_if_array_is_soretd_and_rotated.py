#Problem Link -> https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/974142910/
class Solution:
    def check(self, nums: List[int]) -> bool:
        ans = [0] * len(nums)
        x = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                x = i
                break
       
        for i in range(len(nums)):
            ans[i] = nums[(i+x)%len(nums)]
        
        for i in range(1,len(nums)):
            if ans[i-1] > ans[i]:
                return False
        return True
        
