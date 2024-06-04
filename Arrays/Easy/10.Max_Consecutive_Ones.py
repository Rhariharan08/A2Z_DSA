#Problem Link -> https://leetcode.com/problems/max-consecutive-ones/description/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        maxi =0
        for i in nums:
            if i == 1:
                a += 1
                maxi = max(a,maxi)
            else:
                a = 0
        return maxi
