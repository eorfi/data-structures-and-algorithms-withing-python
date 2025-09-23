class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.next)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev =None
            temp.next = None
        self.length -= 1
        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(index):
                temp = temp.prev
        return temp
            
    def set(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        self.length -= 1 
        return temp

    def is_palindrome(self):
        if self.length <= 1:
            return True
        forword_node = self.head
        backword_node = self.tail
        for i in range(self.length//2):
            if forword_node != backword_node:
                return False
            forword_node = forword_node.next
            backword_node = backword_node.prev
        return True
    
    def reverse(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

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

    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev = dummy
        for _ in range(start_index):
            prev = prev.next
        current = prev.next
        for _ in range(start_index-end_index):
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

    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        if self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            second_node.prev = previous_node
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
            self.head = first_node.next
            previous_node = first_node
        self.head = dummy_node.next
        if self.head:
            self.head.prev = None