# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                if sum_val < 0:
                    j += 1
                elif sum_val > 0:
                    k -= 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    
        return ans
