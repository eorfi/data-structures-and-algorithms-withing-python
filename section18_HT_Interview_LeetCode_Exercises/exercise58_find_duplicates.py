# HT: Find Duplicates ( ** Interview Question)
# find_duplicates()


# Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


# Input:

# A list of integers nums.


# Output:

# A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]
# Explanation: The numbers 2 and 3 appear more than once in the input array.
 
# Input: nums = [1, 2, 3, 4, 5]
# Output: []
# Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
# Input: nums = [3, 3, 3, 3, 3]
# Output: [3]
# Explanation: The number 3 appears more than once in the input array.
 
# Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
# Output: [-1, 0, 2]
# Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
 
# Input: nums = []
# Output: []
# Explanation: There are no numbers in the input array, so the function returns an empty list [].

def find_duplicates(nums):
    # Create an empty dictionary named 'num_counts'.
    # This will be used to keep track of the frequency of each number
    # in the 'nums' list.
    num_counts = {}
 
    # Start a loop that iterates over each number in the 'nums' list.
    for num in nums:
        # For the current number 'num', update its count in the 'num_counts'
        # dictionary. If 'num' is not already in the dictionary, get(num, 0)
        # will return 0. Then, 1 is added to this value, effectively
        # initializing the count to 1 the first time 'num' is encountered.
        # If 'num' is already in the dictionary, its count is incremented by 1.
        num_counts[num] = num_counts.get(num, 0) + 1
#         “Try to get the value of 4 from the dictionary.
# If it doesn’t exist, use 0 instead.”
# num_counts.get(4, 0) → 0 (because dictionary is empty)
# Then 0 + 1 → 1
#“Increase the count of this number by 1,
# or start it at 1 if it wasn’t there before.”
#Your function find_duplicates(nums) is trying to find which numbers appear more than once in a list.
# When you loop through nums, you want to know:
# Did I see this number before?
# If yes → increase its count.
# If no → start counting it (count = 1).

# So num_counts[4] = 1
 
    # Initialize an empty list called 'duplicates'.
    # This list will store all the numbers that appear more than once in 'nums'.
    duplicates = []
 
    # Iterate over each key-value pair in the 'num_counts' dictionary.
    # 'num' is the number from the list, and 'count' is its frequency.
    for num, count in num_counts.items():
        # Check if the count of the current number is greater than 1.
        # A count greater than 1 indicates that the number is a duplicate.
        if count > 1:
            # If the current number is a duplicate, append it to the
            # 'duplicates' list.
            duplicates.append(num)
 
    # After the loop, return the 'duplicates' list, which now contains
    # all numbers that were found more than once in the input list 'nums'.
    return duplicates


# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
 
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
 
#     return duplicates


# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1

#     duplicates = [] 
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates


# def find_duplicates(nums):
#     num_counts = {}
#     for num in num:
#         num_counts[num] = num_counts.get(num, 0) + 1

#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)

#     return duplicates


# def find_duplicated(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1

#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates


# def find_duplicated(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#     duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1

#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates



# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
    
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = nums.get(num, 0) + 1
#     duplicates = []
#     for num, cunt in num_counts.items():
#         if cunt >1:
#             duplicates.append(num)
#     return duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates

# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
#     return duplicates

def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = []
    for num, count in num_counts:
        if count > 1:
            duplicates.append(num)
    return duplicates