# class Node:
# the nodes that we're going to use will be identical to linked list nodes
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        # self.bottom = new_node # you don't really need the bottom for a stack
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp)
            temp = temp.next



my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""