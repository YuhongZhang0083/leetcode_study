'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_new = ""

        for char in s:
            if char.isalnum():
                str_new += char.lower()
        
        reversed_s = str_new[::-1]
        print(reversed_s)

        return reversed_s == str_new
    
    def isPalindrome_pointer(self, s:str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1 
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True




    
s = "Was it a car or a cat I saw?"
s2 = "tab a cat"
sol = Solution()
print(sol.isPalindrome(s))
print(sol.isPalindrome(s2))
print(sol.isPalindrome_pointer(s))
print(sol.isPalindrome_pointer(s2))
