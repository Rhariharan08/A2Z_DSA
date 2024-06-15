# https://leetcode.com/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l , pro , cnt = 0 , 1, 0
        n = len(nums)
        for r in range(n):
            pro = pro * nums[r]
            
            while pro >= k and l <= r:
                pro = pro // nums[l]
                l += 1
            cnt += r - l + 1
        return cnt 
