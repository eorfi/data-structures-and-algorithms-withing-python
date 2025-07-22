my_list = [23, 45, 67, 89, 12]
my_list.append(34)  # O(1) - appending an element to the end of the list
my_list.pop()  # O(1) - removing the last element from the list
my_list.pop(0)  # O(n) - removing the first element from the list, requires shifting all other elements
my_list.insert(0, 99)  # O(n) - inserting an element at the beginning of the list, requires shifting all other 
# and the n is the size of the list

list2 = [1, 2, 3, 4, 5]
list2.insert(1, "Hi") # O(n) - inserting an element at index 1, requires shifting elements