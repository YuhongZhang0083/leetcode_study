'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.


'''


# 1 Naive solution: sort the str, and if not seen, store in dict, finally return the list of the value
class solution1:
    def groupAnagrams(self, strs):
        group = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) #sorted 给出来的是list

            if sorted_word not in group:
                group[sorted_word] = []
            
            group[sorted_word].append(word) #如果 key 不存在：先创建空 list 不管 key 是新建的还是已经存在的：都把 word 加进去


        return list(group.values())


strs = ["act","pots","tops","cat","stop","hat"]
sol1 = solution1()
print(sol1.groupAnagrams(strs))



# optimization: count the frequency of each character in a string

class solution2:
    def groupAnagrams2(self, strs):
        group = {}

        for word in strs:
            count = [0] * 26  # 一个word对应着一个26维的向量

            for char in word:
                index = ord(char) - ord('a') #每一个字符相对于a的位置
                count[index] += 1

            key = tuple(count) #list 不能作为key， immutable tuple可以

            if key not in group: # 如果key不在group里 创建一个空list
                group[key] = []
            
            group[key].append(word)

        return list(group.values())



strs = ["act","pots","tops","cat","stop","hat"]
sol2 = solution2()
print(sol2.groupAnagrams2(strs))
