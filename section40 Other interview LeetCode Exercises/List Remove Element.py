# List: Remove Element ( ** Interview Question)
# Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.

# The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memor

# WRITE THE REMOVE_ELEMENT FUNCTION HERE #
#                                        #
#                                        #
#                                        #
#                                        #
##########################################
# def remove_element(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
#     return k

# def remove_element(nums, val):
#     k = 0
    
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
    
#     # نقصّ الليست بحيث تحتوي فقط على العناصر الصحيحة
#     del nums[k:] # this line removes all elements from index k to the end of the list, effectively resizing the list to contain only the valid elements.
    
#     return k

# def remove_element(nums, val):
#     k = 0

#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
    
#     del nums[k:]
#     return k


def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

# | الحل         | الزمن |
# | ------------ | ----- |
# | بتاعك (pop)  | O(n²) |
# | Two pointers | O(n)  |



# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")

# Test case 2: Removing a value that's located at the end of the list.
nums2 = [1, 2, 3, 4, 5, 6]
val2 = 6
print("\nRemove value", val2, "that's located at the end of the list.")
print("BEFORE:", nums2)
new_length2 = remove_element(nums2, val2)
print("AFTER:", nums2, "\nNew length:", new_length2)
print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3 = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)
print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4 = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)
print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5 = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)
print("-----------------------------------")

