# https://leetcode.com/problems/4sum/description/


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j- 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    tot_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if tot_sum < target:
                        k += 1
                    elif tot_sum > target:
                        l -= 1
                    else:
                        ans.add((nums[i], nums[j] ,nums[k] , nums[l]))
                        k += 1
                        l -= 1
        return ans
