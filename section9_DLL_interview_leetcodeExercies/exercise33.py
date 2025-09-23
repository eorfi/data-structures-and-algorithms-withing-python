# DLL: Partition List ( ** Interview Question)
# Write a method called partition_list(self, x) that rearranges the nodes in a doubly linked list so that all nodes with a value less than a given number x come before all nodes with a value greater than or equal to x.

# You must maintain the original relative order of the nodes in each of the two partitions.

# The partitioning must be performed in-place. You cannot create new nodes (other than dummy nodes).

# Both .next and .prev pointers must be updated correctly.

# If the list is empty, nothing should happen.





# 🧪 Examples

# Example 1
# Input DLL:
# 3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1
# Partition value: x = 5
# Output DLL:
# 3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10

# Why:

# Nodes < 5: 3, 2, 1

# Nodes >= 5: 8, 5, 10

# Order of nodes is preserved in both groups

# Smaller group comes before larger/equal group



# Example 2
# Input DLL:
# 1 <-> 2 <-> 3
# Partition value: x = 5
# Output DLL:
# 1 <-> 2 <-> 3
# Why:
# All nodes are already less than x. No rearrangement needed.



# Example 3
# Input DLL:
# 7 <-> 8 <-> 9
# Partition value: x = 5
# Output DLL:
# 7 <-> 8 <-> 9
# Why:
# All nodes are >= x. Order remains the same.



# Example 4
# Input DLL:
# 1
# Partition value: x = 2
# Output DLL:
# 1
# Why:
# Single-node list. Nothing to rearrange.



# Example 5
# Input DLL:
# (empty)
# Partition value: x = 3
# Output DLL:
# (empty)
# Why:
# Empty list. Nothing to do.





# 📘 What This Exercise Is Designed to Teach

# How to traverse and reorganize nodes in a doubly linked list.

# How to use dummy nodes to simplify pointer manipulation.

# How to maintain both .next and .prev pointers correctly in DLLs.

# How to perform an in-place partition without losing any nodes.

###############################################################################

# # hints:
# 📋 Pseudocode Outline

# Create two dummy nodes:

# One for the list of nodes less than x (dummy1).

# One for the list of nodes greater than or equal to x (dummy2).

# Use two pointers prev1 and prev2 to build each list.

# Traverse the original list:

# If a node’s value is less than x, attach it to the end of the first list.

# Otherwise, attach it to the end of the second list.

# After traversal:

# Connect the two lists.

# Set the new head of the list to the first dummy's .next.

# Ensure .prev pointers are correctly reassigned.

# End the new list with None.





# 💡 Hints

# Dummy nodes help avoid special cases for the head pointer.

# Be careful to update both .next and .prev when rearranging nodes.

# When connecting the two lists, ensure the first list points to the beginning of the second list.

# Do not leave dangling .next or .prev pointers at the end.

# The first dummy node itself should not be part of the final list — only its .next.





# 📊 Step-by-Step Example (Visual Walkthrough)

# Input List:
# 3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1

# Partition value x = 5

# Nodes less than 5: 3, 2, 1

# Nodes greater than or equal to 5: 8, 5, 10

# Build two lists during traversal:

# First list:
# 3 <-> 2 <-> 1

# Second list:
# 8 <-> 5 <-> 10

# Then connect them:

# Final list:
# 3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10

# -------------------------------


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

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    # def partition_list(self, x):

        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Partitions a doubly linked list around a value  |
        #   |   `x`.                                            |
        #   | - All nodes with values less than `x` come before |
        #   |   nodes with values greater than or equal to `x`. |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - Uses two dummy nodes to create two sublists:    |
        #   |   one for nodes < x, and one for nodes >= x.      |
        #   | - Each node is added to the appropriate sublist   |
        #   |   while maintaining both next and prev pointers.  |
        #   | - The sublists are then joined together.          |
        #   | - The head of the list is updated to the start of |
        #   |   the merged result.                              |
        #   +===================================================+

        # if self.head is None:
        #     return

        # # Create two dummy nodes
        # less_head = Node(0)
        # greater_head = Node(0)
        # less = less_head
        # greater = greater_head

        # current = self.head
        # while current is not None:
        #     if current.value < x:
        #         less.next = current
        #         current.prev = less
        #         less = less.next
        #     else:
        #         greater.next = current
        #         current.prev = greater
        #         greater = greater.next
        #     current = current.next

        # # Connect the two sublists
        # greater.next = None
        # less.next = greater_head.next
        # if greater_head.next is not None:
        #     greater_head.next.prev = less

        # # Update the head
        # self.head = less_head.next
        # if self.head is not None:
        #     self.head.prev = None


    # def partition_list(self, x):
    #     # ------------------------------------------------
    #     # If the list is empty, return immediately
    #     # Nothing to partition
    #     # ------------------------------------------------
    #     if not self.head:
    #         return None
    
    #     # ------------------------------------------------
    #     # Create two dummy nodes to serve as the starting
    #     # points for the two new partitions
    #     # dummy1 → nodes with values < x
    #     # dummy2 → nodes with values ≥ x
    #     # ------------------------------------------------
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    
    #     # ------------------------------------------------
    #     # prev1 tracks the end of the < x partition
    #     # prev2 tracks the end of the ≥ x partition
    #     # ------------------------------------------------
    #     prev1 = dummy1
    #     prev2 = dummy2
    
    #     # Start at the head of the original list
    #     current = self.head
    
    #     # ------------------------------------------------
    #     # Traverse the original list and divide nodes
    #     # into two separate partitions based on their value
    #     # ------------------------------------------------
    #     while current:
    #         if current.value < x:
    #             # ----------------------------------------
    #             # Append current node to the < x list
    #             # Update pointers to maintain .next/.prev
    #             # ----------------------------------------
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             # ----------------------------------------
    #             # Append current node to the ≥ x list
    #             # Update pointers to maintain .next/.prev
    #             # ----------------------------------------
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    
    #         # Move to the next node in the original list
    #         current = current.next
    
    #     # ------------------------------------------------
    #     # Terminate the ≥ x list to prevent cycle or
    #     # trailing data from previous .next values
    #     # ------------------------------------------------
    #     prev2.next = None
    
    #     # ------------------------------------------------
    #     # Connect the two partitions:
    #     # Link the end of the < x list to the beginning
    #     # of the ≥ x list
    #     # ------------------------------------------------
    #     prev1.next = dummy2.next
    
    #     # ------------------------------------------------
    #     # If the ≥ x list has at least one node,
    #     # update its .prev to point to the < x list
    #     # ------------------------------------------------
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    
    #     # ------------------------------------------------
    #     # Update the head of the list to the start of
    #     # the < x partition (after dummy1)
    #     # ------------------------------------------------
    #     self.head = dummy1.next
    
    #     # ------------------------------------------------
    #     # Ensure the new head has no previous pointer
    #     # (important for DLL structure)
    #     # ------------------------------------------------
    #     self.head.prev = None

    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current 
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next 
    #     prev2.next = None # this line is to terminate the second list
    #     # Connect the two lists 
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None
    
    # def partion_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    # def partition_list(self,x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current 
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #         prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    # def parition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None
        
    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #         prev2.next = None
    #         prev1.next = dummy2.next
    #         if dummy2.next:
    #             dummy2.next.prev = prev1
    #         self.head = dummy1.next
    #         self.head.prev = None
    
    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value < x:
    #             prev1.next = current
    #             current.prev = prev1
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             current.prev = prev2
    #             prev2 = current
    #         current = current.next
    #     prev2.next = None
    #     prev1.next = dummy2.next
    #     if dummy2.next:
    #         dummy2.next.prev = prev1
    #     self.head = dummy1.next
    #     self.head.prev = None

    def partition_list(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next
        prev2.next = None
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        self.head = dummy1.next
        self.head.prev = None


# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

