'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current_num = num
            current_longest = 1


            while current_num + 1 in nums:
                current_num += 1
                current_longest += 1

            longest = max(longest, current_longest)    

        return longest
    
    def longestConsecutive2(self, nums: List[int]) -> int:

        '''
        Is there any way to identify the start of a sequence? For example, in [1, 2, 3, 10, 11, 12], only 1 and 10 are the beginning of a sequence. 
        Instead of trying to form a sequence for every number, we should only consider numbers like 1 and 10.
        '''
        
        longest = 0
        num_set = set(nums)
        for num in num_set:
            current_num = num
            current_longest = 1

            if num - 1 not in num_set:
                while current_num + 1 in num_set:
                    current_num += 1
                    current_longest += 1
                longest = max(longest, current_longest)
        return longest

    
nums = [2,20,4,10,3,4,5]
nums2 = [0,3,2,5,4,6,1,1]

sol = Solution()
print(sol.longestConsecutive(nums))
print(sol.longestConsecutive(nums2))

print(sol.longestConsecutive2(nums))
print(sol.longestConsecutive2(nums2))