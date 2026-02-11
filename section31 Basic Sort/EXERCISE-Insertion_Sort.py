## WRITE INSERTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 

# def insertion_sort(my_list):
#         for i in range(1, len(my_list)): # we starting form the second index , to the end of the list
#                 temp = my_list[i]
#                 j = i - 1 # TO COMPARE WITH THE INDEX BEFORE IT
#                 while temp < my_list[j] and j > -1:
#                         my_list[j+1] = my_list[j]
#                         my_list[j] = temp
#                         j -= 1
#         return my_list


# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i -1
#         while  temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list
      
# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i - 1
#         while temp < my_list[j] and j > - 1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list

# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i - 1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list

# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i - 1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list


# def insertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i - 1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list


# def inssertion_sort(my_list):
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i - 1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list

def insertion_list(my_list):
    for i in range(my_list):
        temp = my_list[i]
        j = i -1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

