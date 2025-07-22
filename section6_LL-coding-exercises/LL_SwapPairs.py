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
 

        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Swaps adjacent pairs of nodes in a singly linked|
        #   |   list by modifying the next pointers.            |
        #   |                                                   |
        #   | Parameters:                                       |
        #   | - None: Operates on the linked list's head.       |
        #   |                                                   |
        #   | Return:                                           |
        #   | - None: Modifies the linked list in place.        |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - If the list is empty or has one node, no swaps  |
        #   |   are performed.                                  |
        #   | - For each pair of adjacent nodes, swaps their    |
        #   |   positions by updating the next pointers.        |
        #   | - Uses a dummy node to simplify handling of the   |
        #   |   head node swap.                                 |
        #   | - Iterates through the list using a first pointer,|
        #   |   keeping the head unchanged until the final      |
        #   |   update.                                         |
        #   | - Sets the head to the new first node at the end. |
        #   +===================================================+
# # this is the copilot solution
#     def swap_pairs(self):
#         if not self.head or not self.head.next:
#             return

#         dummy = Node(0)
#         dummy.next = self.head
#         prev = dummy
#         current = self.head

#         while current and current.next:
#             first = current
#             second = current.next

#             # Swapping
#             prev.next = second
#             first.next = second.next
#             second.next = first

#             # Move pointers forward
#             prev = first
#             current = first.next

#         self.head = dummy.next
        
# this is hintes 
# 📋 Pseudocode Outline

# Create a dummy node and point its .next to the head

# Initialize two pointers:

# previous starts at the dummy node

# first starts at the head

# While first and first.next exist:

# Let second be first.next

# Perform swapping:

# previous.next = second

# first.next = second.next

# second.next = first

# Move previous to first

# Move first to first.next

# After loop ends, update self.head = dummy.next





# 💡 Hints

# Changing the next pointers carefully is critical.

# Save the next node before making any pointer updates.

# Dummy nodes make head swaps easier without special cases.





# 📊 Step-by-Step Example (Visual Walkthrough)

# Original List:

# 1 → 2 → 3 → 4 → None

# After swap_pairs(), it should become:

# 2 → 1 → 4 → 3 → None

# Walkthrough:

# First pair: 1 and 2 → swap → 2 → 1

# Second pair: 3 and 4 → swap → 4 → 3

# Result: 2 → 1 → 4 → 3 → None

# If odd number of nodes, final node is not swapped.
 

    # def swap_pairs(self):
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     previous = dummy
    #     first = self.head

    #     while first and first.next:
    #         second = first.next

    #         # Perform the swap
    #         previous.next = second
    #         first.next = second.next
    #         second.next = first

    #         # Move pointers
    #         previous = first
    #         first = first.next

    #     self.head = dummy.next

    # def swap_pairs(self):
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     previous = dummy
    #     first = self.head

    #     while first and first.next:
    #         second = first.next
            
        #     previous.next = second
        #     first.next = second.next
        #     second.next = first

        #     previous = first 
        #     first = first.next

      # self.head = dummy.next

# def swap_pairs(self):
#     dummy = Node(0)
#     dummy.next = self.head
#     previous = dummy
#     first = self.head

#     while first and first.next:
#         second = first.next

#         previous.next = second
#         first.next = second.next
#         second.next = first

#         previous = first
#         first = first.next
#     self.head = dummy.next

# def swap_pairs(self):
#     dummy = Node(0)
#     dummy.next = self.head
#     previous = dummy
#     first = self.head

#     while first and first.next:
#         second = first.next

#         previous = second.next
#         first.next = second.next
#         second.next = first

#         previous = first
#         first = first.next
#     self.head = dummy.next

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = self.head

        while first and first.next:
            second = first.next

            previous.next = second.next
            first.next = second.next
            second.next = first

            previous = first
            first = first.next
        self.head = dummy.next


# Test case 1: Swapping pairs in a list with an even number of nodes (1->2->3->4)
print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("BEFORE: ", end="")
ll1.print_list()
print("AFTER:  ", end="")
ll1.swap_pairs()
ll1.print_list()
print("-----------------------------------")

# Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
print("BEFORE: ", end="")
ll2.print_list()
print("AFTER:  ", end="")
ll2.swap_pairs()
ll2.print_list()
print("-----------------------------------")

# Test case 3: Swapping pairs in a list with a single node (1)
print("\nTest case 3: Swapping pairs in a list with a single node.")
ll3 = LinkedList(1)
print("BEFORE: ", end="")
ll3.print_list()
print("AFTER:  ", end="")
ll3.swap_pairs()
ll3.print_list()
print("-----------------------------------")

# Test case 4: Swapping pairs in an empty list
print("\nTest case 4: Swapping pairs in an empty list.")
ll4 = LinkedList(1)
ll4.make_empty()
print("BEFORE: ", end="")
ll4.print_list()
print("AFTER:  ", end="")
ll4.swap_pairs()
ll4.print_list()
print("-----------------------------------")

# Test case 5: Swapping pairs in a list with two nodes (1->2)
print("\nTest case 5: Swapping pairs in a list with two nodes.")
ll5 = LinkedList(1)
ll5.append(2)
print("BEFORE: ", end="")
ll5.print_list()
print("AFTER:  ", end="")
ll5.swap_pairs()
ll5.print_list()
print("-----------------------------------")


