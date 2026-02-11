# Stack: Sort Stack
# the way to do it is to use another stack to help sort the original stack
# and pop elements from the original stack and push them to the helper stack
# if the top of the helper stack is greater than the element to be pushed


# Stack: Sort Stack ( ** Interview Question)
# The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 
# The function should use the pop, push, peek, and is_empty methods of the Stack object.
# Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.
# This will use the Stack class we created in these coding exercises:
# The function should perform the following tasks:
# Create a new instance of the Stack class called sorted_stack.
# While the input stack is not empty, perform the following:
# Pop the top element from the input stack and store it in a variable temp.
# While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.
# Push the temp variable onto the sorted_stack.
# Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.
# You can also click on "Hints" (above) to see the pseudo-code.
# Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.


# Pseudo Code:
# 1. Create a new temporary stack for sorting, called 'sorted_stack'.
# 2. While the input stack is not empty:
#    a. Pop the top element from the input stack, store it in 'temp'.
#    b. While the 'sorted_stack' is not empty and its top element is greater than 'temp':
#        i. Pop the top element from 'sorted_stack' and push it back onto the input stack.
#    c. Push 'temp' onto the 'sorted_stack'.
# 3. Transfer elements back from 'sorted_stack' to the input stack:
#    a. While 'sorted_stack' is not empty:
#        i. Pop the top element from 'sorted_stack' and push it onto the input stack.


# Time complexity: O(n^2)
# Space complexity: O(n)

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################

def sort_stack(stack):
    additional_stack = Stack()
 
    while not stack.is_empty():
        temp = stack.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())


# The sort_stack function sorts a given stack of integers in ascending order using only one additional stack. Here's how it works:
# First, the function creates a new stack called additional_stack to hold the sorted elements.
# Next, the function enters a while loop that continues until the original stack is empty. Inside the loop, the function removes the top element from the original stack using the pop method and stores it in a temporary variable called temp.
# The function then enters another while loop that continues until the additional_stack is empty or the top element of additional_stack is less than or equal to temp. Inside the loop, the function removes the top element from the additional_stack using the pop method and adds it back to the original stack using the push method.
# Once the inner while loop is exited, the function adds the temp variable to the additional_stack using the push method. This ensures that the additional_stack is always sorted in ascending order.
# Once the outer while loop is exited, the function enters another while loop that continues until the additional_stack is empty. Inside the loop, the function removes the top element from the additional_stack using the pop method and adds it back to the original stack using the push method. This step ensures that the original stack is sorted in ascending order.
# Finally, the function returns the sorted stack.
# Overall, this implementation has a time complexity of O(n^2), where n is the number of elements in the original stack, because the function performs nested loops to compare all the elements with each other. However, it has the advantage of using only one additional stack, which could be useful in certain situations where memory is limited.
# Code with inline comments:

# def sort_stack(stack):
#     # Create a new stack to hold the sorted elements
#     additional_stack = Stack()
 
#     # While the original stack is not empty
#     while not stack.is_empty():
#         # Remove the top element from the original stack
#         temp = stack.pop()
 
#         # While the additional stack is not empty and 
#         #the top element is greater than the current element
#         example: if the current element is 3 and the top of the additional stack is 5 therefore we need to move 5 back to the original stack
#         while not additional_stack.is_empty() and additional_stack.peek() > temp: # peek() returns the top element of the stack without removing it
#             # Move the top element from the additional stack to the original stack
#             stack.push(additional_stack.pop())
 
#         # Add the current element to the additional stack
#         additional_stack.push(temp) # if temp > additional_stack.peek() then we can push it directly to the additional stack
 
#     # Copy the sorted elements from the additional stack to the original stack
#     while not additional_stack.is_empty():
#         stack.push(additional_stack.pop())





my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""