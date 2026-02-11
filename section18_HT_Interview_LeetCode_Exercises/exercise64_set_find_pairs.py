
# Set: Find Pairs ( ** Interview Question)
# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values

# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
# def find_pairs(arr1, arr2, target):
#     pairs = []
#     set_arr2 = set(arr2)  # Convert arr2 to a set for O(1) lookups
    
#     for num1 in arr1:
#         complement = target - num1
#         if complement in set_arr2:
#             pairs.append((num1, complement))
    
#     return pairs

def find_pairs(arr1, arr2, target):
    pairs = []
    set_arr2 = set(arr2)
    for num1 in arr1:
        complement = target - num1
        if complement in set_arr2:
            pairs.append((num1, complement))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""