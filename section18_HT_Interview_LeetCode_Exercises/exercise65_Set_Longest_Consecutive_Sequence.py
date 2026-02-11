# Set: Longest Consecutive Sequence ( ** Interview Question)
# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""