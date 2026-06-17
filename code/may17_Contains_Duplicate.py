

# brute force
# time complexity: O(n^2), every element needs to compare with the element after it
# space complexity: O(1), no array creation or hash table 

class Solution:
    def hasDuplicate(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False
                
#test case
sol = Solution()
nums = [1, 2, 3, 3]
print(sol.hasDuplicate(nums))

nums1 = [1, 2, 3, 4]
print(sol.hasDuplicate(nums1))



'''
optimization using set, no duplicate allowed in a set
scan from left to right
if this number seen previously, means duplicate, return true
if not, add to seen set
if scan done, and no duplicate, then return false

Hash set can be so fast because it uses a hash table internally. A hash table uses a hash function to map an element to a specific location in memory. 
It is similar to finding a drawer directly based on its label instead of searching every drawer one by one. Therefore, a statement like 3 in seen is not a linear scan.

For space complexity, the line seen = set() stores additional data. In the worst case, for example nums = [1, 2, 3, 4, 5], 
there are no duplicates, so the set will eventually become seen = {1, 2, 3, 4, 5}. Since the set stores up to n elements, the space complexity is O(n).

because it uses additional memory to reduce computation time. This is a classic example of a space-time tradeoff: using memory to reduce computation.
'''

class Solution2:
    def hasDuplicate2(self, nums):
        seen = set() #define an empty set

        for num in nums:
            if num in seen: 
                return True
            else:
                seen.add(num)
        return False
    

sol2 = Solution2()
print(sol2.hasDuplicate2(nums))
print(sol2.hasDuplicate2(nums1))


