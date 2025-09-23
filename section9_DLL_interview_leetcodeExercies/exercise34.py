# DLL: Reverse Between ( ** Interview Question)
# Write a method reverse_between that reverses a portion of a doubly linked list in place.

# You are given a start index and an end index (inclusive range). Reverse only the nodes between those indices.

# Indexing is zero-based.

# The list is made of nodes with both next and prev pointers.

# Make sure the list remains fully connected after the reversal in both directions.

# If the list has fewer than two nodes or the start and end indices are the same, leave the list unchanged.





# Examples

# Input:  1 <-> 2 <-> 3 <-> 4 <-> 5,  start_index = 1, end_index = 3  
# Output: 1 <-> 4 <-> 3 <-> 2 <-> 5
 
# Input:  10 <-> 20 <-> 30 <-> 40,  start_index = 0, end_index = 2  
# Output: 30 <-> 20 <-> 10 <-> 40
 
# Input:  1,  start_index = 0, end_index = 0  
# Output: 1




# 📘 What This Exercise Is Designed to Teach

# How to manipulate pointers in a doubly linked list

# Understanding in-place reversal using node repositioning

# Careful edge case handling in linked list algorithms

# hints:
# 📋 Pseudocode Outline

# If list has 1 or 0 nodes → return

# Create a dummy node before head

# Traverse to the node just before start_index (call it prev)

# Set current to prev.next

# Repeat for (end_index - start_index):

# Temporarily detach node_to_move = current.next

# Move node_to_move after prev

# Fix both next and prev pointers

# Update the head pointer to dummy.next

# Set head.prev = None to detach dummy





# 💡 Hints

# Use a dummy node to simplify pointer management, especially when reversing includes the head

# Detach and re-insert nodes during each loop to reverse order

# Remember to update both .next and .prev pointers

# After reversal, check if head changed and update it





# 📊 Step-by-Step Example (Visual Walkthrough)

# Input

# List: 3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1
# Reverse between index 1 and 4

# Before:

# Index:  0     1     2      3     4     5
#         3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1
# After:

# 3 <-> 2 <-> 10 <-> 5 <-> 8 <-> 1
# Reversed portion: 8, 5, 10, 2 → becomes 2, 10, 5, 8



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = current
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

        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Reverses a segment of a doubly linked list      |
        #   |   between the given start_index and end_index.    |
        #   | - This operation modifies only the segment in     |
        #   |   place, preserving the rest of the list.         |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - A dummy node is used to simplify edge cases     |
        #   |   like reversing from the head.                   |
        #   | - The `prev` pointer moves to the node before     |
        #   |   the reversal section.                           |
        #   | - The segment is reversed by removing nodes one   |
        #   |   at a time and reinserting them at the front of  |
        #   |   the sublist.                                    |
        #   | - All `next` and `prev` pointers are updated      |
        #   |   carefully to maintain list integrity.           |
        #   | - At the end, the new head is set properly and    |
        #   |   its prev pointer is cleared.                    |
        #   +===================================================+



    # 🔧 Code with Inline Comments



    # def reverse_between(self, start_index, end_index):
    #     # ---------------------------------------------
    #     # Reverses the portion of the list between the
    #     # given start_index and end_index in-place.
    #     # Assumes 0-based indexing.
    #     # ---------------------------------------------
    
    #     # If the list has 0 or 1 nodes, or no change needed
    #     if self.length <= 1 or start_index == end_index:
    #         return
    
    #     # Create a dummy node before head to simplify edge cases
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     self.head.prev = dummy
    
    #     # Traverse to the node just before the start_index
    #     prev = dummy
    #     for _ in range(start_index):
    #         prev = prev.next
    
    #     # current points to the first node in the segment to reverse
    #     current = prev.next
    
    #     # Reverse the segment using node splicing
    #     for _ in range(end_index - start_index):
    #         node_to_move = current.next
    
    #         # Detach node_to_move from its current position
    #         current.next = node_to_move.next
    #         if node_to_move.next:
    #             node_to_move.next.prev = current
    
    #         # Insert node_to_move right after prev
    #         node_to_move.next = prev.next
    #         prev.next.prev = node_to_move
    #         prev.next = node_to_move
    #         node_to_move.prev = prev
    
    #     # Update head pointer in case it was changed
    #     self.head = dummy.next
    # #     self.head.prev = None

    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1 or start_index == 0:
    #         return
        
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     self.head.prev = dummy

    #     prev = dummy
    #     for _ in range(start_index):
    #         prev = prev.next
        
    #     current = prev.next

    #     for _ in range(end_index-start_index):
    #         node_to_move = current.next

    #         current.next = node_to_move.next
    #         if node_to_move.next:
    #             node_to_move.next.prev = current

    #         node_to_move.next = prev.next
    #         prev.next.prev = node_to_move
    #         prev.next = node_to_move
    #         node_to_move.prev = prev

    #     self.head = dummy.next
    #     self.head.prev = None

    # def reverse_between(self, start_index, end_index):
    #     if self.length <= 1 or start_index==end_index:
    #         return
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     self.head.prev = dummy

    #     prev = dummy
    #     for _ in range(start_index):
    #         prev = prev.next
    #     current = prev.next

    #     for _ in range(end_index-start_index):
    #         node_to_move = current.next

    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return # in this line i use return just return nothing
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev = dummy
        for _ in range(start_index):
            prev = prev.next
        current = prev.next
        for _ in range(end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev
        self.head = dummy.next
        self.head.prev = None


# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()

