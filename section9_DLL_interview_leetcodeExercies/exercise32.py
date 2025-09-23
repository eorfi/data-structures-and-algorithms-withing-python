# DLL: Reverse ( ** Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

# Do not change the value of any of the nodes.

# Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.

# Pseudo-code can be found under "Hints" (above).

##########################################################

# hints:

# Pseudo code for the reverse method:def 

# Set current_node to head

# While current_node is not None:

# Set a temporary variable, temp_next, to current_node.next

# Set current_node.next to current_node.prev

# Set current_node.prev to temp_next

# Set current_node to temp_next (which is actually the previous node after swapping)

# Swap head and tail pointers of the DoublyLinkedL


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    ## WRITE REVERSE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################

    # def reverse(self):
    #     if self.head is None:
    #         return
        
    #     current = self.head
    #     prev_node = None
        
    #     while current is not None:
    #         next_node = current.next
    #         current.next = prev_node
    #         current.prev = next_node
    #         prev_node = current
    #         current = next_node
            
    #     self.head, self.tail = self.tail, self.head


    # def reverse(self):
    #     # Initialize 'temp' to point to the list's head.
    #     # 'temp' is used to traverse the list.
    #     temp = self.head

    #     # Loop until 'temp' is None, signifying the
    #     # end of the list has been reached.
    #     while temp is not None:
    #         # Swap the current node's 'prev' and 'next'.
    #         # This reverses the link direction for the node.
    #         # 'prev' becomes 'next', and vice versa.
    #         temp.prev, temp.next = temp.next, temp.prev
        
    #         # Move to the next node in the original list
    #         # order to continue the reversal.
    #         # After swapping, 'prev' points to the next
    #         # node in original order, so move to 'temp.prev'.
    #         temp = temp.prev
        
    #     # After reversing all nodes, update the list's
    #     # head and tail to reflect the new order.
    #     # The original head is now the tail, and the
    #     # original tail is now the head.
    #     self.head, self.tail = self.tail, self.head
    #     # End of reverse method

    # def reverse(self):
    #     temp = self.head
    #     while temp:
    #         temp.prev, temp.next = temp.next, temp.prev
    #         temp = temp.prev
    #     self.head, self.tail = self.tail, self.head


    # def reverse(self):
    #     temp = self.head
    #     while temp:
    #         temp.prev, temp.next = temp.next, temp.prev
    #         temp = temp.prev
    #     self.head , self.tail = self.tail, self.head

# def reverse(self):
#     temp = self.head
#     while temp:
#         temp.prev, temp.next = temp.next, temp.prev
#         temp = temp.prev
#     self.head, self.tail = self.tail, self.head


# def reverse(self):
#     temp = self.head
#     while temp:
#         temp.prev, temp.next = temp.next, temp.prev
#         temp = temp.prev
#     self.head, self.tail = self.tail, self.head

    def reverse(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
        

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1 <-> 2 <-> 3 <-> 4 <-> 5
    
    DLL after reverse():
    5 <-> 4 <-> 3 <-> 2 <-> 1

"""

