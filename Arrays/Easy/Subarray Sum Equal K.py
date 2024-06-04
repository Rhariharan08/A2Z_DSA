https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        PrefixSum = {0:1}
        Total = 0
        Count = 0
        for num in nums:
            Total += num

            if Total in PrefixSum:
                PrefixSum[Total] += 1
            else:
                PrefixSum[Total] = 1
                
            if Total-k in PrefixSum:
                Count += PrefixSum[Total-k]
            
            
        
        return Count
