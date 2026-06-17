# Minimum Window Substring


'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        window = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
        
        have = 0
        need_count = len(need)

        left = 0
        res = ""
        res_len = float("inf") # 找最小值的时候，经常这样写 999999

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]: #?
                have += 1

            while have == need_count:
                if right - left + 1 < res_len: # 1 < 99999
                    res_len = right - left + 1 
                    res = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        return res



sol = Solution()
s = "OUZODYXAZV"
t = "XYZ"

print(sol.minWindow(s,t))
        

