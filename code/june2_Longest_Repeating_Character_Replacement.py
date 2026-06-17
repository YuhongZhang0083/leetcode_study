'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        res = 0

        for right in range(len(s)): #right 一步一步往右走，把新字符加入窗口。
            char = s[right]

            count[char] = count.get(char, 0) + 1 # 记录当前窗口里这个字符出现次数 +1。

            max_count = max(max_count, count[char]) # 更新窗口里出现最多的字符次数。

            window_length = right - left + 1 # 计算当前窗口长度。

            while window_length - max_count > k:  # 如果：窗口长度 - 最多字符次数 > k 说明需要替换的字符太多，窗口不合法。
                count[s[left]] -= 1 # 所以缩小左边：意思是把最左边字符移出窗口。
                left += 1
                window_length = right - left + 1 # 然后重新计算窗口长度：

            res = max(res, window_length) # 如果当前窗口合法，就更新最长长度。

        return res