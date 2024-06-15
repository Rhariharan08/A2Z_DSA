# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        maxlen = 0
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            maxlen = max(maxlen, r-l+1)
        return maxlen
