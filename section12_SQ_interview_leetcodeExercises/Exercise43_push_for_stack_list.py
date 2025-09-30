# Stack: Push for Stack That Uses List ( ** Interview Question)
# Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.
# Remember: This Stack implementation uses a list instead of a linked list.


class Stack:
    def __init__(self):
        self.stack_list = []
        
    # def print_stack(self):
    #     for i in range(len(self.stack_list)-1, -1, -1): # -1 -1 -1 means start at the end of the list and go backwards
    #         print(self.stack_list[i])
    
    # anther way to write print_stack method
    # more easy and pythonic print form top to bottom
    def print_stack(self):
        for item in reversed(self.stack_list):
            print(item)


    # WRITE PUSH METHOD HERE #
    #                        #
    #                        #
    #                        #
    ##########################
    def push(self, value):
        self.stack_list.append(value)
    



my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1
 
"""
