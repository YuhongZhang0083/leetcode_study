
'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

对于每一个位置 i：

    重新遍历整个 nums

    把除了 nums[i] 以外的所有数字乘起来

    放到 output[i]

'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []

        for i in range(n):
            product = 1

            for j in range(n):
                if i != j:
                    num = nums[j]
                    product *= num

            res.append(product)

        return res

sol = Solution()
nums = [1,2,4,6]
print(sol.productExceptSelf(nums))
nums = [-1,0,1,2,3]
print(sol.productExceptSelf(nums))


class Solution2:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n

        res = [1] * n

        for i in range(1,n): # prefix[i] = product of all numbers before i
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1): # suffix[i] = product of all numbers after i
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n): # result[i] = left product * right product
            res[i] = prefix[i] * suffix[i]

        return res

sol2 = Solution2()
nums = [1,2,4,6]
print(sol2.productExceptSelf2(nums))
nums = [-1,0,1,2,3]
print(sol2.productExceptSelf2(nums))

