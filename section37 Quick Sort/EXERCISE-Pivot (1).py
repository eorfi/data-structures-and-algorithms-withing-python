def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


## WRITE PIVOT FUNCTION HERE ##
#                             #
#                             #
#                             #
#                             #
############################### 
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1 
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index # we not returnig the value but we are returning the index of it


# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index
        
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index


# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot

#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index

# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index, end_index):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap_index(my_list, pivot_index, swap_index)
#     return swap_index

# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, 1)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index

# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1 
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index


# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index+1, end_index+1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(pivot_index, swap_index)
    return swap_index

my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nPivot Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Pivot Index:
    3

 """