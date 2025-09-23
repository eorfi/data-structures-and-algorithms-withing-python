def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# the drop non dominant term it is O(n) + O(n) = O(2n) = O(n)
# This is a linear time complexity, as the constant factor is dropped in Big O notation.
# it is two loops make the same time complexity as one loop
# bec both of them looping through the same n




print_items(10)

