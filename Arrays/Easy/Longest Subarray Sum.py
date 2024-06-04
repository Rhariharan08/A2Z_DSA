from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    PrefixSum = {0:1}
    Tot = 0
    MaxLen = 0
    for index in range(len(nums)):
        Tot += nums[index]

        if Tot == k:
            MaxLen = max(MaxLen, index+1)

        if Tot - k in PrefixSum:
            Len = index - PrefixSum[Tot-k]
            MaxLen = max(MaxLen, Len)
        
        if Tot not in PrefixSum:
            PrefixSum[Tot] = index
        
    return MaxLen
