# Stack: Reverse String ( ** Interview Question)
# The reverse_string function takes a single parameter string, which is the string you want to reverse.
# Return a new string with the letters in reverse order.
# This will use the Stack class we created in the last three coding exercises:

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



## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
#########################################

    # def reverse_string(self, string):
    #     Stack = Stack()
    #     for i in string:
    #         Stack.push(i)
    #     reversed_str = ""
    #     while not Stack.is_empty():
    #         reversed_str += Stack.pop()
    #     return reversed_str
    

    # def reverse_string(self,string):
    #     stack = Stack()
    #     for i in string:
    #         stack.push(i)
    #     reversed_str = ""
    #     while not stack.is_empty():
    #         reversed_str += stack.pop()
    #     return reversed_str

    # def reverse_string(string):
    #     stack = Stack()
    #     reversed_string = ""
    
    #     for char in string:
    #         stack.push(char)
    
    #     while not stack.is_empty():
    #         reversed_string += stack.pop()
    
    #     return reversed_string
    
    def reverse_string(string):
        stack = Stack()
        reversed_str = ""
        for i in string:
            stack.push(i)
        while not stack.is_empty():
            reversed_str+= stack.pop()
        return reversed_str


my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
