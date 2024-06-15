# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        tot = 0
        cnt = 0
        r = 0
        while r < len(arr):

            if r - l + 1 > k:
                tot -= arr[l]
                l += 1
            
            tot += arr[r]

            if r-l+1 == k and (tot/k) >= threshold:
                cnt += 1
            
            r+=1
        
        return cnt
