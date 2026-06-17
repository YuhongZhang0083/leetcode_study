

'''
brute force
sort the string and compare. Note, sort() and .sort() are different
nums = [3, 1, 2]
nums.sort()

字符串没有 .sort()：
s = "racecar"
s.sort()  # 报错
因为字符串是 immutable，也就是不能原地修改。


n = len(s)
m = len(t)
O(n log n + m log m)
sorted(s)
O(n log n)
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
    

sol = Solution()
s = "racecar"
t = "carrace"
s1 = "jar"
t1 = "jam"

print(sol.isAnagram(s,t))
print(sol.isAnagram(s1,t1))



# optimization using dict(), hash table, a string that contains the exact same characters as another string , order is not important

class Solution2:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for char in s: 
            count_s[char] = count_s.get(char, 0) + 1  # 如果 char 已经在 dict 里面，取它现在的次数 如果不在，就当作 0. 这个字符出现次数 +1
        
        for char in t:
            count_t[char] = count_t.get(char,0) + 1

        return count_s == count_t
    
sol2 = Solution2()
s = "racecar"
t = "carrace"
s1 = "jar"
t1 = "jam"

print(sol2.isAnagram2(s,t))
print(sol2.isAnagram2(s1,t1))
