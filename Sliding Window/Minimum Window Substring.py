# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
    
        # Create a dictionary to count characters in t
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # Variables to keep track of the required number of unique characters
        required = len(char_count_t)
        formed = 0
        
        # Array to keep track of counts of characters in the current window
        window_counts = [0] * 128  # Assuming ASCII characters
        
        # Sliding window pointers
        left, right = 0, 0
        
        # Result tuple (window length, left, right)
        ans = float("inf"), 0, 0
        
        # Start sliding the window
        while right < len(s):
            char = s[right]
            window_counts[ord(char)] += 1
            
            if char in char_count_t and window_counts[ord(char)] == char_count_t[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[ord(char)] -= 1
                if char in char_count_t and window_counts[ord(char)] < char_count_t[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
