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
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    #   +===================================================+
    #   |                  WRITE YOUR CODE HERE             |
    #   | Description:                                      |
    #   | - This method removes all nodes with duplicate    |
    #   |   values from the linked list.                    |
    #   | - It keeps track of seen values with a set.       |
    #   | - If a value is repeated, it is skipped over by   |
    #   |   changing the 'next' pointer of the previous     |
    #   |   node, effectively removing the duplicate.       |
    #   | - The list's length is adjusted for each removed  |
    #   |   duplicate.                                      |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We maintain a 'previous' node as a reference    |
    #   |   to re-link the list when skipping duplicates.   |
    #   | - The 'current' node iterates through the list.   |
    #   | - The 'values' set holds unique items seen so far.|
    #   +===================================================+
    # def remove_duplicates(self):
    #     if self.head is None:
    #         return  # Empty list, nothing to do

    #     current = self.head
    #     previous = None
    #     values = set()

    #     while current is not None:
    #         if current.value in values:
    #             # Duplicate found, skip it
    #             previous.next = current.next
    #             self.length -= 1
    #         else:
    #             # Not a duplicate, add to set and move previous pointer
    #             values.add(current.value)
    #             previous = current
            
    #         # Move to the next node
    #         current = current.next

    
# Solution using nested loops:

    # def remove_duplicates(self):
    #     current = self.head
    #     while current:
    #         # Start checking from the next node
    #         runner = current
    #         while runner.next:
    #             # If the next node's value matches current's value, skip it
    #             if runner.next.value == current.value:
    #                 runner.next = runner.next.next
    #                 self.length -= 1
    #             else:
    #                 runner = runner.next
    #         current = current.next

    # def remove_duplicates(self):
    #     current = self.head
    #     while current:
    #         runner = current
    #         while runner.next:
    #             if runner.next.value == current.Value:
    #                 runner.next = runner.next.next
    #                 self.length -= 1
    #             else:
    #                 runner = runner.next
    #         current = current.next

    # def remove_duplicates(self):
    #     current = self.head
    #     while current:
    #         runner = current
    #         while runner.next:
    #             if runner.next.value == current.value:
    #                 runner.next = runner.next.next
    #                 self.length -= 1
    #             else:
    #                 runner = runner.next
    #         current = current.next

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
    # Solution using a set:

    # def remove_duplicates(self):
    #         values = set() # Create an empty set to store unique values
    #         previous = None # Previous node to keep track of the last unique node
    #         current = self.head # Start with the head of the linked list
    #         while current:
    #             if current.value in values: # If the current value is already in the set
    #                 previous.next = current.next
    #                 self.length -= 1
    #             else:
    #                 values.add(current.value) # Add the current value to the set
    #                 previous = current # Update the previous node to the current node
    #             current = current.next

    # def remove_duplicates(self):
    #     values = set()
    #     previous = None
    #     current = self.head
    #     while current:
    #         if current.value in values:
    #             previous.next = current.next
    #             self.length -= 1
    #         else:
    #             values.add(current.value)
    #             previous = current
    #         current = current.next

    # def remove_duplicates(self):
    #     values = set()
    #     previous = None
    #     current = self.head
    #     while current:
    #         if current.value in values:
    #             previous.next = current.next
    #             self.length -= 1
    #         else:
    #             values.add(current.value)
    #             previous = current
    #         current = current.next

    def remove_duplucates(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

# The Set
# values = set() creates an empty set to store unique values we encounter in the linked list

# Sets are perfect for this because they only store unique elements and provide O(1) lookup time

# How It Works:
# We traverse the linked list with current pointer

# For each node:

# If we've seen the value before (it's in the set), we "remove" the node by making the previous node skip it

# If it's a new value, we add it to the set and update our previous pointer

# The algorithm maintains the order of first occurrences while removing later duplicates

# Time Complexity:
# O(n) time - we visit each node exactly once

# O(n) space - in the worst case we might store all values in the set

# This is an efficient way to remove duplicates while preserving the original order of the remaining elements.     


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0   # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])
