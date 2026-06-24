'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
'''
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*","/"}: # 弹两个、算、压回（注意顺序和除法取整）
                b = stack.pop() # right oprand 
                a = stack.pop() # left oprand 

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(b / a) # 除法要「向零取整」
                
                stack.append(result)

            else: #数字 转int 压入
                num = int(token)
                stack.append(num)
        
        return stack[-1] #最后一个值就是结果

s = Solution()
tokens = ["1","2","+","3","*","4","-"]
print(s.evalRPN(tokens))
                