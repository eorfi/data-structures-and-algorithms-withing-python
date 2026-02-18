# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def find_max_min(nums):
    if len(nums) == 0:
        return None
    maximum = nums[0]
    minimum = nums[0]
    for i in range(len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
        if nums[i] < minimum:
            minimum = nums[i]
    return (maximum, minimum)



print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""