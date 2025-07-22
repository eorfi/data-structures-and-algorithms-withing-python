#the linked list is like a dictionary, where each node points to the next node
# somthing like this:
# head = {'value': 1, 'next':
#           {'value': 2, 'next':
#             {'value': 3, 'next':
#                 {'value': 4, 'next':
#                     {'value': 5, 'next':
#                     None}}}}}
# print(head['next']['next']['next']['value'])  # Output: 3
# or 
# This is will only work if the linked list is not empty
# print(my_linked_list.head.next.next.value)  # Output: 3

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linked_List:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
# mylinkedlist = Linked_List(1)
# print(mylinkedlist.tail.value)

# LL: Constructor
# class Node:
#     def __init__(self, value):
#         self. value = value
#         self.next = None

# class Linked_List:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
# MyLinkedList = Linked_List(69)
# print(MyLinkedList.head.value)


# linked list print list
# class Node:
#     def __init__(self, value):
#         self. value = value
#         self.next = None

# class Linked_List:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
    
    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.head)
    #         temp = temp.next

    # # append
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node

        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next
        
    
    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    # append
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is not None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else: 
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1
    #     return True

    # def append(self):
    #     new_node = Node(self)
    #     if self.head is  None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
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
            self.tail = new_node
        self.length += 1
        return True

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp
    
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head == None
    #         self.tail == None
    #     return temp

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return None

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp
    
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while (temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next -= 1
    #     if self.length == 0:
    #         return None
    #     return temp
      
    # def pop(self):
    #     if self.pop == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     pre = self.head 
    #     while(self.next):
    #         pre = temp
    #         temp = self.next
    #     self.tail = pre
    #     self.tail.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head 
        pre = self.head
        while(self.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        return True
    
    # def prepend(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.length += 1
    #     return True

    # def prepend(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.length += 1 
    #     return True

    # def prepend(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.length += 1
    #     return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # def pop_first(self):
    #     if self.length == 0: # if the linked list is empty
    #         return None
    #     # we have 2 sinarios here:
    #     # 1. if the linked list has only one node
    #     # 2. if the linked list has more than one node
    #     # the two scenarios are handled by the same code
    #     temp = self.head # store the current head node
    #     self.head = self.head.next # move the head pointer to the next node
    #     temp.next = None # disconnect the old head node from the list
    #     self.length -= 1 # decrease the length of the linked list
    #     if self.length == 0: # if the linked list is now empty
    #         self.tail = None 
    #     return temp

    # def pop_first(self):
    #     if self.length == 0:
    #         self.head = None
    #     temp = self.head
    #     self.head = self.head.next
    #     temp.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.tail = None
    #     return temp

    # def pop_first(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     self.head = self.head.next
    #     temp.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.tail = None
    #     return temp 

    # def pop_first(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.head
    #     self.head = self.head.next
    #     temp.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.tail = None
    #     return temp

    # def get(self, index):
    #     if index < 0 or index >= self.length: # index out of bounds
    #         return None
    #     temp = self.head # start from the head node
    #     for _ in range(index):# iterate to the desired index
    #         temp = temp.next # move to the next node
    #     return temp # return the node at the desired index

    # def get(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     temp = self.head
    #     for _ in range(index):
    #         temp = temp.next
    #     return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # def set_value(self, index, value):
    #     temp = self.get(index) # get the node at the desired index
    #     if temp is not None:
    #         temp.value = value
    #         return True # if the index is valid
    #     return False # if the index is out of bounds

    # def set_value(self, index, value):
    #     temp = self.get(index)
    #     if temp is not None:
    #         temp.value = value
    #         return True
    #     return False
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # def insert(self, index, value):
    #     if index < 0 or index > self.length: # index out of bounds
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)
    #     # insert in the middle
    #     new_node = Node(value) # create a new node
    #     temp = self.get(index - 1) # get the node before the desired index
    #     new_node.next = temp.next # point the new node to the next node
    #     temp.next = new_node # point the previous node to the new node
    #     self.length += 1 # increase the length of the linked list
    #     return True

    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(index)
    #     if index == self.length:
    #         return self.append(index)
    #     new_node = Node(value)
    #     temp = self.get(index -1)
    #     new_node.next = temp.next
    #     temp.next = new_node
    #     self.length += 1
    #     return True 

    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)
    #     new_node = None(value)
    #     temp = self.get(index-1)
    #     new_node.next = temp.next
    #     self.length +=1
    #     return True
        
    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.lenght:
    #         return self.append(value)
    #     new_node = Node(value)
    #     temp = self.get(index-1)
    #     new_node.next = temp.next
    #     temp.next = new_node
    #     self.length += 1
    #     return True

    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)
    #     new_node = Node(value)
    #     temp = self.get(index-1)
    #     new_node.next = temp.next
    #     temp.next = new_node
    #     self.length += 1
    #     return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
        # def remove(self, index): 
        #     if index < 0 or index > self.length: # index out of bounds
        #         return None
        #     if index == 0: # if you want to remove the first node
        #         return self.pop_first() 
        #     if index == self.length-1:  # if you want to remove the last node
        #         return self.pop()
        #     # remove from the middle
        #     prev = self.get(index-1)
        #     temp = prev.next
        #     prev.next = temp.next
        #     temp.next = None
        #     self.length -= 1
        #     return temp

    # def remove(self, index):
    #     if index < 0 or index > self.length:
    #         return None
    #     if index == 0:
    #         return self.pop_first()
    #     if index == self.length-1:
    #         return self.pop()
    #     prev = self.get(index-1)
    #     temp = prev.next
    #     prev.next = temp.next
    #     temp.next = None
    #     self.length -= 1
    #     return temp

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prve = self.get(index-1)
        temp = prve.next
        prve.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     after = temp.next
    #     before = None
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp 
    #         temp = after

    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     after = temp.next
    #     before = None
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after

    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     after = temp.next
    #     before = None
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    class LinkedList:
        def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        def print_list(self):
            temp = self.head
            if temp:
                print(temp.value)
                temp = temp.next

        def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
            return True
        
        def pop(self):
            if self.length == 0:
                return None
            temp = self.head
            pre = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
        
        def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                self.head.next = new_node
                new_node = self.head
            self.length += 1

        def pop_first(self):
            if self.length == 0:
                return None
            temp = self.head
            self.head.next = self.head
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
        
        def get(self, index):
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
        def set_value(self, value, index):
            temp = self.get(index)
            if temp:
                temp.value = value
                return True
            return False
        
        def insert(self, index, value):
            if index < 0 or index > self.length:
                return False
            if index == 0:
                return self.prepend(value)
            if index == self.length:
                return self.append(value)
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

        def remove(self, index):
            if index < 0 or index > self.length:
                return None
            if index == 0:
                return self.pop_first
            if index == self.length-1:
                return self.pop
            prve = self.get(index-1)
            temp = prve.next
            prve.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

        def reverse(self):
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp 
                temp = after
    
    # this is the full code of the liked list

# MyLinkedList = Linked_List(69)
# MyLinkedList.append(2)
# MyLinkedList.print_list()

my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


my_linked_list.prepend(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()