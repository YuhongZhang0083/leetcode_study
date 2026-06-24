'''
Valid Parentheses

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false

'''


class solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(','}':'{',']':'['}
 
        for char in s:
            if char in "([{":
                stack.append(char)
            else: #当前是右括号
                if not stack: #栈空的情况 栈空：右括号来了，但没东西可弹（数量上右括号多了）。比如 ")"、"())"。
                    return False
                top = stack.pop()

                if top != pair[char]:
                    return False
                
        return not stack #栈空了 返回1 true
    
    
        
    

     