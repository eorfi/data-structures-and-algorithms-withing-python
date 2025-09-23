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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #   +===================================================+
    #   |               WRITE YOUR CODE HERE                |
    #   | Description:                                      |
    #   | - This method partitions a linked list around a   |
    #   |   value `x`.                                      |
    #   | - It rearranges the nodes so that all nodes less  |
    #   |   than `x` come before all nodes greater or equal |
    #   |   to `x`.                                         |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
    #   |   to build two separate lists: one for elements   |
    #   |   smaller than `x` and one for elements greater   |
    #   |   or equal to `x`.                                |
    #   | - `prev1` and `prev2` help us keep track of the   |
    #   |   last nodes in these lists.                      |
    #   | - Finally, we merge these two lists by setting    |
    #   |   `prev1.next = dummy2.next`.                     |
    #   | - The head of the resulting list becomes          |
    #   |   `dummy1.next`.                                  |
    #   +===================================================+


    # def partition_list(self, x):
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head

    #     while current:
    #         next_node = current.next
    #         current.next = None
    #         if current.value < x:
    #             prev1.next = current
    #             prev1 = prev1.next
    #         else:
    #             prev2.next = current
    #             prev2 = prev2.next
    #         current = next_node

    #     prev1.next = dummy2.next
    #     self.head = dummy1.next

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
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             prev2 = current
    #         current = current.next
    
    #     prev1.next = dummy2.next #     # Connect the end of the < x list to the start of the >= x list
    #     prev2.next = None #     # Disconnect the end of the >= x list to prevent cycles
    
    #     self.head = dummy1.next #      # Update the head of the linked list to the start of the partitioned list

    # def partition_list(self,x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value > x:
    #             prev1.next = current
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             prev2 = current
    #         current.next = current
    #     prev1.next = dummy2.next
    #     prev2.next = None
        
    #     self.head = dummy1.next #       # Update the head of the linked list to the start of the partitioned list
        
    # def partition_list(self,x):
    #     if not self.head:
    #         return None
    #     dummy1 = Node(0)
    #     dummy2 = Node(0)
    #     prev1 = dummy1
    #     prev2 = dummy2
    #     current = self.head
    #     while current:
    #         if current.value > x:
    #             prev1.next = current
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             prev2 = current
    #         current = current.next
    #     prev1.next = prev2.next
    #     prev2.next = None  # Disconnect the end of the >= x list to prevent cycles
    #     self.head = dummy1.next  # Update the head of the linked list to the start of the partitioned list

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
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             prev2 = current
    #         current = current.next
    #     prev1.next = prev2.next
    #     prev2.next = None

    #     self.head = dummy1.next

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
    #             prev1 = current
    #         else:
    #             prev2.next = current
    #             prev2 = current
    #         current = current.next
    #     prev1.next = dummy2.next
    #     prev2.next = None
    #     self.head = dummy1.next

    def partition_list(self,x):
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
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = dummy2.next
        prev2.next = None

        self.head = dummy1.next

# As you work through the pseudo-code, I recommend sketching the nodes, pointers, and each step on paper. This visual representation will greatly aid in understanding and tracking the process.


# 📋 Pseudocode Outline

# Define the method partition_list that takes self and x as arguments.

# Check if the head of the linked list is None (empty list):

# If it is, return None and exit the method.

# Create two dummy nodes with value 0:

# dummy1: will be the head of the "less than x" list.

# dummy2: will be the head of the "greater than or equal to x" list.

# Initialize two pointers:

# prev1 starts at dummy1 (used to build the < x list).

# prev2 starts at dummy2 (used to build the ≥ x list).

# Set a pointer current to the head of the original list.

# Loop while current is not None:

# a. If current.value < x:

# i. Point prev1.next to current.

# ii. Move prev1 forward to current.

# b. Else (i.e., current.value >= x):

# i. Point prev2.next to current.

# ii. Move prev2 forward to current.

# c. Move current to the next node in the original list.

# After the loop ends:

# Disconnect the last node of the ≥ x list:

# Set prev2.next = None.

# Link the two lists:

# Connect the last node of the < x list (prev1.next) to the head of the ≥ x list (dummy2.next).

# Update the original list:

# Set self.head = dummy1.next to complete the partitioning.




# 💡 Hints

# You need to preserve the original relative order of the nodes in each partitioned list (less than x and greater than or equal to x).

# Use two dummy nodes to build two separate lists:

# One for nodes with values less than x

# One for nodes with values greater than or equal to x

# Keep two pointers (prev1, prev2) to track the tails of these new lists as you build them.

# As you loop through the original list, place each node into one of the two lists based on its value.

# At the end, connect the end of the < x list to the start of the ≥ x list.

# Don’t forget to set the end of the ≥ x list to None to prevent accidental cycles in the list.

# You only need to rearrange the nodes — do not create new nodes for existing values.


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      