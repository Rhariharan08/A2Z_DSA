# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        Ans = 0
        while l < r:

            Ans = max(Ans, ((r-l)*min(height[l],height[r])))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return Ans
