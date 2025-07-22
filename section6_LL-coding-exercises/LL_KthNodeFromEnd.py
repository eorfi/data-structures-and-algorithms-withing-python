class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  

  
 
  
    #### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
    #                                             #
    #    This is a SEPARATE FUNCTION that         #
    #    is NOT a method within the               #
    #    LinkedList class.                        #
    #                                             #
    #    <== INDENT ALL THE WAY TO THE LEFT.      #
    #                                             #
    ###############################################
# def find_kth_from_end(ll, k):
#     slow = ll.head
#     fast = ll.head
#     for _ in range(k):
#         if fast is None:
#             return None
#         fast = fast.next
#     while fast is None: 
#         slow = slow.next
#         fast = fast.next # why i move the fast pointer only once?
#     # The fast pointer moves k steps ahead, then both pointers move at the same speed.
#     return slow
    
# def find_kth_from_end(ll, k):
#     slow = ll.head
#     fast = ll.head
#     for _ in range(k):
#         if fast is None:
#             return None
#         fast = fast.next
#     while fast is not None:
#         slow = slow.Next
#         fast = fast.Next
#     return slow

# def find_kth_from_end(ll, k):
#     slow = ll.head
#     fast = ll.head
    
#     # Move fast pointer k steps ahead
#     for _ in range(k):
#         if fast is None:
#             return None  # k is larger than the length of the list
#         fast = fast.next
    
#     # Move both pointers until fast reaches the end
#     while fast is not None:
#         slow = slow.next
#         fast = fast.next
    
#     return slow  # slow is now at the kth node from the end 
# slow is the pointer that will end up at the kth node from the end of the list.

# def find_kth_from_end(ll, k):
#     slow = ll.head
#     fast = ll.head
#     for _ in range(k):
#         if fast is None:
#             return None
#         fast = fast.next
#     while fast is not None:
#         slow = slow.next
#         fast = fast.next
#     return slow

# Pseudo Code:

# initialize slow and fast pointers to the head of the linked list



# for i in range k:

#     if fast pointer is None:

#         return None (list is shorter than k)

#     move fast pointer to the next node



# while fast pointer is not None:

#     move slow pointer to the next node

#     move fast pointer to the next node


# def find_kth_from_end(ll, k):
#     slow = ll.head
#     fast = ll.head
#     for _ in range(k):
#         if fast is None:
#             return None
#         fast = fast.next
#     while fast:
#         slow = slow.next
#         fast = fast.next
#     return slow


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

# return the slow pointer (k-th node from the end)

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

