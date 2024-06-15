# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c_freq = {}
        longest_str_len = 0
        for r in range(len(s)):

            c_freq[s[r]] = c_freq.get(s[r], 0)+1

            cells_count = r -l + 1
            if cells_count - max(c_freq.values()) <= k:
                longest_str_len = max(longest_str_len, r-l+1)
            else:
                c_freq[s[l]] -= 1
                if not  c_freq[s[l]]:
                    c_freq.pop(s[l])
                l += 1
        
        return longest_str_len
