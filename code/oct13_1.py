

def reverse_array(a: list) -> None:
    """
    Reverses the given array.

    Args:
    a (list): The array to be reversed.

    Returns:
    list: The reversed array.
    """
    i, j = 0, len(a) - 1
    while i<j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# Example usage:
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]


def remove_element(nums: list[int], val: int) -> int:
    k = 0                                # slow pointer: position to overwrite
    for x in nums:                       # fast pointer: reads each value
        if x != val:
            nums[k] = x                  # copy valid element forward
            k += 1
    return k      

# Example usage:
nums = [3, 2, 2, 3]
val = 3
new_length = remove_element(nums, val)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [2, 2]
print(nums)  # Output: [2, 2, 2, 3]



#--------- very big sum -------------
def aVeryBigSum(ar):
    # Write your code here
    n_raw = input().strip()          # first line: "n"
    arr_line = input().strip()       # second line: the n space-separated integers

    print(f"[debug] n_raw={n_raw}")
    print(f"[debug] arr_line='{arr_line}'")

    n = int(n_raw)
    arr = list(map(int, arr_line.split()))


    if len(arr) != n:
        raise ValueError(f"Expected {n} integers, got {len(arr)}")
    
    sum_arr = sum(arr)
    return sum_arr 

# Example usage:
# Input:
# 5
# 1000000001 1000000002 1000000003 100000000004 1000000005
# Output: 5000000015

# result = aVeryBigSum(None)
# print(result)  # Output: 5000000015

#--------- very big sum end -------------


import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    # Write your code here
    max_height = 0
    for ch in word:
        index = ord(ch) - ord('a')
        height = h[index]
        if height > max_height:
            max_height = height
    area = max_height * len(word)
    return area     


def designerPdfViewer_v2(h, word):
    # Write your code here
    heights = []
    for c in word:
        heights.append(h[ord(c) - ord('a')])
    
    tallest = max(heights)
    area = tallest * len(word)
    return area     

# Example usage:
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 5]
word = "zaba"
result = designerPdfViewer(h, word)
print(result)  # Output: 28 (7*4=28)    

result = designerPdfViewer_v2(h, word)
print(result)  # Output: 28 (7*4=28)    










#--------- left rotation -------------
def rotLeft(a, d):
    n = len(a)
    if n == 0:
        return a
    d %= n                 # normalize rotations
    return a[d:] + a[:d]   # left rotation by d

# Example usage:
a = [1, 2, 3, 4, 5]
d = 2

rotated_array = rotLeft(a, d)
print(rotated_array)  # Output: [3, 4, 5, 1, 2]
#--------- left rotation end -------------


# -------- review list -------------
# c = list(range(5))     # c = [0, 1, 2, 3, 4]
# print(c)
# b = c[1:4]      # b = [1, 2, 3
# print(b)
# b1 = c[:3]  
# b2 = c[::2]
# b3 = c[::-1]
# print(b1)
# print(b2)
# print(b3)  # b1 = [1, 3]



arr = [10, 20, 30, 40, 50]

add = lambda x, y: x + y
print(add(1,3))

square = lambda x: x * x
print(list(map(square, arr)))  # Output: [100, 400, 900, 1600, 2500]



from functools import reduce
product = reduce(lambda x, y: x * y, arr)
print(product)  # Output: 12000000  
# -------- review list end -------------


# -------- review dictionary -------------
student = {"name": "Alice", "age": 21, "major": "CS"}
print(student["name"])  # "Alice"

student["GPA"] = 3.9
student["age"] = 22

for key, value in student.items():
    print(f"{key}: {value}")

if "major" in student:
    print("Major is present.")

del student["GPA"]
print(student)
# -------- review dictionary end -------------


"ell" in "hello"               # True        (substring test)
print("ell" in "hello")
"hello".startswith("he")       # True
print("hello".startswith("he"))
"hello".endswith(("lo","xo"))  # True (tuple = any of)
print("hello".endswith(("lo","xo")))
"hello".find("ll")             # 2 (or -1 if not found)
print("hello".find("ll"))
"hello".index("ll")            # 2 (raises ValueError if not found)
print("hello".index("ll"))

# -------- review type conversion -------------

int("123")          # 123
int("ff", 16)       # 255 (base given)
str(123)            # "123"
f"{123}"            # "123" (f-string)



",".join(["a", "b", "c"])       # 'a,b,c'
" ".join(["hello", "world"])    # 'hello world'
"\n".join(["line1", "line2"])   # 'line1\nline2'
"".join(['H','e','l','l','o'])  # 'Hello'