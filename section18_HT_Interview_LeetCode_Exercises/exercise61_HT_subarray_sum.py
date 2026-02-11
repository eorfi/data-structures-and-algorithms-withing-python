# HT: Subarray Sum ( ** Interview Question)
# Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
# def subarray_sum(nums, target):
#     sum_map = {}
#     current_sum = 0
#     for i, num in enumerate(nums):
#         current_sum += num
#         if current_sum == target:
#             return [0, i]
#         complement = current_sum - target
#         if complement in sum_map:
#             return [sum_map[complement] + 1, i]
#         sum_map[current_sum] = i
#     return []

# def subarray_sum(nums, target):
#     sum_map = {}
#     current_sum = 0
#     for i, num in enumerate(nums):
#         current_sum += num
#         if current_sum == target:
#             return [0, i]
#         complement = current_sum - target
#         if complement in sum_map:
#             return [sum_map[complement] + 1, i]
#         sum_map[current_sum] = i
#     return []

def subarray_sum(nums, target):
    sum_map = {}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum == target:
            return [0, i]
        complement = current_sum - target
        if complement in sum_map:
            return [sum_map[complement] + 1, i]
        sum_map[current_sum] = i
    return []




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
