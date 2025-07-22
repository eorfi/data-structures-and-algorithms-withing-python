class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    # def reverse_between(self, left, right):
    #     if self.head is None or left == right or self.length == 0:
    #         return

    #     dummy = Node(0)
    #     dummy.next = self.head
    #     prev = dummy

    #     # Move prev to the node before the 'left' position
    #     for _ in range(left):
    #         if prev.next is None:
    #             return
    #         prev = prev.next

    #     # Reverse the sublist from left to right
    #     curr = prev.next
    #     for _ in range(right - left):
    #         if curr is None or curr.next is None:
    #             break
    #         temp = curr.next
    #         curr.next = temp.next
    #         temp.next = prev.next
    #         prev.next = temp

    #     # Update head if needed
    #     self.head = dummy.next

        # this is copoilot code:
        
#     # this is the hints:
#     Pseudo Code:
# 1. Function reverse_between(start_index, end_index):

#     1.1 Check if length of list <= 1

#         1.1.1 If true, return (do nothing)

       

#     1.2 Create dummy node with value 0

#     1.3 Point dummy node's next to head of list

#     1.4 Initialize previous_node to dummy node



#     1.5 Loop for start_index times to find previous_node

#         1.5.1 Update previous_node to its next node

       

#     1.6 Initialize current_node to previous_node's next node



#     1.7 Loop from 0 to (end_index - start_index)

#         1.7.1 Initialize node_to_move to current_node's next

#         1.7.2 Update current_node's next to node_to_move's next

#         1.7.3 Update node_to_move's next to previous_node's next

#         1.7.4 Update previous_node's next to node_to_move

   

#     1.8 Update head to dummy_node's next node







# Explained another way:


# Let's imagine our code is like a game where you have a line of toy blocks connected with string (that's our linked list).

# Each block has a number, starting from 0, to help us find its place.



# Start and End Points: The game's mission is to flip some of these blocks from a starting point (start_index) to an ending point (end_index).

# Is the Line too Short?: First, the game checks if you have only one or zero blocks. If that's the case, there's nothing to flip, so the game does nothing.

# Dummy Block: Next, the game adds an extra "dummy" block at the beginning. This is like a helper block to make sure everything goes smoothly.

# Finding the Block Before Start: The game finds the block right before where you want to start flipping. This block is called the previous_node.

# Finding the Start Block: The first block you actually want to flip is called the current_node, and it comes right after the previous_node.

# Flipping Time: Now, the fun part!

# The game takes the block right after current_node (we call this one node_to_move).

# It unhooks node_to_move and moves it to be right after the previous_node.

# It keeps doing this until it reaches the end_index.

# Clean-Up: At the end, the game removes the extra "dummy" block and makes sure the first block in the line is correct.



# And there you go! The blocks between the start_index and end_index are now flipped in reverse order.
    
# the solution
    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1:
    #         return # If the list is empty or has only one element, do nothing
    
    #     dummy_node = Node(0)
    #     dummy_node.next = self.head
    #     previous_node = dummy_node
    
    #     for i in range(start_index):
    #         previous_node = previous_node.next
    
    #     current_node = previous_node.next
    
    #     for i in range(end_index - start_index):
    #         node_to_move = current_node.next
    #         current_node.next = node_to_move.next
    #         node_to_move.next = previous_node.next
    #         previous_node.next = node_to_move
    # in here, first we create a dummy node to handle edge cases easily, then we find the previous node to the start index, and then we reverse the nodes between start and end indices.
    #     # Finally, we update the head of the linked list to point to the new
    
    #     self.head = dummy_node.next  

    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1:
    #         return
    #     dummy_node = Node(0)
    #     dummy_node.next = self.head
    #     previous_node = dummy_node
    #     for i in range(start_index):
    #         previous_node = previous_node.next
    #     current_node = previous_node.next

    #     for i in range(end_index-start_index):
    #         node_to_move = current_node.next
    #         current_node.next = node_to_move.next
    #         node_to_move.next = previous_node.next
    #         previous_node.next = node_to_move
    #     self.head = dummy_node.next

    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1:
    #         return
    #     dummy_node = Node(0)
    #     dummy_node.next = self.head
    #     previous_node = dummy_node

    #     for i in range(start_index):
    #         previous_node = previous_node.next
    #     current_node = previous_node.next

    #     for i in range(end_index-start_index):
    #         node_to_move = current_node.next
    #         current_node.next = node_to_move.next
    #         node_to_move.next = previous_node.next
    #         previous_node.next = node_to_move
    #     self.head = dummy_node.next


    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1:
    #         return
    #     dummy_node = Node(0)
    #     dummy_node.next = self.head
    #     previous_node = dummy_node

    #     for i in range(start_index):
    #         previous_node = previous_node.next
    #     current_node = previous_node.next

    #     for i in range(end_index-start_index):
    #         node_to_move = current_node.next
    #         current_node.next = node_to_move.next
    #         node_to_move.next = previous_node.next
    #         previous_node.next = node_to_move
    #     self.head = dummy_node.next

    def reverse_between(self, start_index, end_index):
        dummy_node = None(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        
        for i in range(start_index):
            previous_node = previous_node.next
        current_node = previous_node.next

        for i in range(end_index-start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
        self.head = dummy_node.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""