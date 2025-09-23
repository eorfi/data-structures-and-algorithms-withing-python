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
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################


    
    # def find_middle_node(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
    
    # def find_middle_node(self):
    #     fast = self.head
    #     slow = self.head
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
#         return slow
        
    # def find_middle_node(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
        
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None: # in this line why am doing fast.next is not None --> to avoid error when fast is at the last node and we try to access fast.next.next which will give error as fast.next is None ***
            slow = slow.next
            fast = fast.next.next
        return slow





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""