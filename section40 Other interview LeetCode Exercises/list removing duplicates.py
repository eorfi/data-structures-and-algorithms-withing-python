# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
# def remove_duplicates(my_list):
#     if not my_list:
#         return None
#     x = len(my_list)
#     y = 0
#     current = my_list[y]
#     for i in range(1 ,len(my_list)):
#         if y > x:
#             return
#         if current == my_list[i]:
#             del current
#         current = my_list[y+1]
#     return len(my_list)
            
def remove_duplicates(my_list):
    if not my_list:
        return 0
    
    k = 1  # first unique element is always at index 0

    for i in range(1, len(my_list)):
        if my_list[i] != my_list[k-1]: # this line to check if the current element is different from the last unique element
            # why doing k-1 because k is the index of the next unique element, so k-1 is the index of the last unique element
            my_list[k] = my_list[i]
            k += 1
    
    return k

# [ منطقة نظيفة | منطقة لسه بنتفحصها ]
# ضغطنا العناصر الـ unique في أول الليست
# ورجعنا عددهم (k)

            
    


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


