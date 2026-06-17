
'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]

'''

# 1. naive solution would be sort the array based on rfequency of each element, and we select top k frequent elements

class solution1:
    def topKfrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_items = sorted(count.items(), key=lambda x: x[1],  reverse=True) #从大往小排
        print(sorted_items)

        res = []

        for i in range(k): #从大往小选
            res.append(sorted_items[i][0])

        return res


    # 2. 使用bucket sort algorithm 
    def topKfrequent_bucket(self, nums, k):
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([]) 
        
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []

        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res



sol = solution1()
nums = [1,2,2,3,3,3]
k = 2
print(sol.topKfrequent(nums,k)) 



# def topKfrequent_bucket(self, nums, k):
#     # Create a dictionary to store the frequency of each number
#     # key = number, value = frequency
#     count = {}
    
#     # Count how many times each number appears in nums
#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     # Create buckets.
#     # bucket[i] will store all numbers that appear exactly i times.
#     bucket = []

#     # We need len(nums) + 1 buckets because the maximum frequency can be len(nums)
#     for i in range(len(nums) + 1):
#         bucket.append([]) 
    
#     # Put each number into the bucket corresponding to its frequency
#     for num, freq in count.items():
#         bucket[freq].append(num)

#     # Store the final top k frequent elements
#     res = []

#     # Scan buckets from high frequency to low frequency
#     for freq in range(len(bucket) - 1, 0, -1):

#         # Add all numbers with this frequency
#         for num in bucket[freq]:
#             res.append(num)

#             # Once we collect k elements, return the result
#             if len(res) == k:
#                 return res


