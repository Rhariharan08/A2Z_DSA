# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = maxRight = 0
        res = 0

        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    res += (maxLeft - height[l])
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    res += (maxRight - height[r])
                r -= 1
        return res
