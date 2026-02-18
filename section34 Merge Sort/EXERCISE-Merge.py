
## WRITE MERGE FUNCTION HERE ##
#                             #
#                             #
#                             #
#                             #
############################### 
# def merge(list1, list2):
#     combined = []
#     i = 0 # the first item from the frist list
#     j = 0 # the fitst item from the second list 
#     while i < len(list1) and j < len(list2): # that mens when the 2 list stil has itesm in them
#         if list1[i] < list2[j]:
#             combined.append(list1[i])
#             i += 1
#         else:
#             combined.append(list2[j])
#             j += 1
#     while i < len(list1):
#         combined.append(list1[i])
#         i+= 1
#     while j < len(len(list2[j])):
#         combined.append(list2[j])
#         j += 1
#     return combined

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else: 
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """