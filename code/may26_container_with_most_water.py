

'''
水的高度由较短的 bar 决定。

如果移动较高的边，短板不变，宽度还变小，面积不可能变大。

所以只能尝试移动较短边。
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1,7,2,5,4,7,3,6]
sol = Solution()
print(sol.maxArea(height))    
            


