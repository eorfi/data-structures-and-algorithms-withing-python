# 1 DLL: Constructor
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None # This is the previous pointer for the doubly linked list 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# class DoublyLinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp)
        
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp)
            temp.next
    
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         new_node.prev = self.tail
    #         self.tail = new_node
    #     self.length += 1

    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         new_node.prev = self.tail
    #         self.tail = new_node
    #     self.length += 1
    #     return True
    
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         new_node.prev = self.tail
    #         self.tail = new_node
    #     self.length += 1
    #     return True

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            