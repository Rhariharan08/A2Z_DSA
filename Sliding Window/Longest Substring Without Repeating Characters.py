# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        char_values = [-1] * 255
    
        l = 0
        maxlen = 0

        for r in range(len(s)):
            char_val = ord(s[r])
            # If the character was seen before and is within the current window
            if char_values[char_val] >= l:
                l = char_values[char_val] + 1
            # Update the last seen index of the character
            char_values[char_val] = r
            # Update the maximum length found
            maxlen = max(maxlen, r - l + 1)

        return maxlen
