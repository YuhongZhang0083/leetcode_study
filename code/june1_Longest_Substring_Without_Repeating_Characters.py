'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        seen = set()
        longest = 0

        for right in range(n):
            #如果当前字符已经在窗口里，就不断从左边移除字符，直到当前字符不重复。
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            current_length = right - left + 1
            longest = max(longest, current_length)
        
        return longest

sol = Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))

s = "xxxx"
print(sol.lengthOfLongestSubstring(s))