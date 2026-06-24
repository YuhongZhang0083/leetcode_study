
from typing import List

# brute force, double loop  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]
                if sum == target:

                    return [i, j]

sol = Solution()
nums = [3,4,5,6]
target = 7
print(sol.twoSum(nums, target))


# optimization
class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {} # or seen = dict()

        for i in range(n):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]
            
            seen[nums[i]] = i

sol2 = Solution2()
nums = [3,4,5,6]
target = 7
print(sol2.twoSum2(nums, target))
'''
先检查：我需要的另一个数 difference，之前有没有见过？

如果见过：

    直接返回“之前那个数的 index”和“当前数的 index”

如果没见过：

    把当前数存进 seen，留给后面的数字使用
'''


# question variant: not limit to two sum, what about n-sum?

class solution3:
    def two_sum_two_pointers(self, nums, start, target):
        # nums sorted
        res = []

        left = start
        right = len(nums) - 1

        while left < right:
            sums = nums[left] + nums[right]

            if sums == target:
                res.append([nums[left] , nums[right]])

                #append 完了之后还要 让指针继续往后
                left += 1
                right -= 1

            elif sums < target:
                left += 1

            else:
                right -= 1
        return res
    
    def n_sum(self, nums, n, start, target):

        res = []

        if n == 2:
            return self.two_sum_two_pointers(nums, start, target)
        
        for i in range(start,len(nums)):

            new_target = target - nums[i]
            sub_result = self.n_sum(nums, n-1, i+1, new_target)

            for sub in sub_result:
                res.append([nums[i]] + sub)

        return res


sol3 = solution3()
nums = [1, 2, 3, 4, 5]
nums.sort() #在调用前sort
n = 3
target = 12
print(sol3.n_sum(nums, 3, 0, target))




    




