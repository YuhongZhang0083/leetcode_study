

'''
Permutation in String
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        count_s1 = {}
        count_s2 = {}

        # count frequency of s1
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        # initialize first window in s2
        for i in range(n1):
            char = s2[i]
            count_s2[char] = count_s2.get(char, 0) + 1

        if count_s1 == count_s2:
            return True
        
        for right in range(n1, n2):
            left = right - n1

            # add new right character
            count_s2[s2[right]] = count_s2.get(s2[right], 0) + 1

            # remove old left character
            count_s2[s2[left]] -= 1

            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]

            if count_s1 == count_s2:
                return True
        return False
              

s1 = "abc"
s2 = "lecaabee"

sol = Solution()
print(sol.checkInclusion(s1, s2))