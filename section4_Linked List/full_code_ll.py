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
        while temp:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

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
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
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
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
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
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
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
    
    def find_minddle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            return False

    def find_kth_from_end(ll,k):
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
    
    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current.next:
            num = num * 2 + current.value
            current = current.next
        return num
    
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
                prev1.next =current
                prev1 = current
            else:
                prev2.next =current
                prev2 = current
            current = current.next
        prev1.next = dummy2.next
        prev2.next = None
        self.head = dummy1.next

    def reverse_between(self, sart_index, end_index):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        for i in range(sart_index):
            previous_node = previous_node.next
        current_node = previous_node.next
        for i in range(end_index- sart_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
        self.head = dummy_node.next

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        first = self.head
        while first and first.next:
            second = first.next
            prev.next = second.next
            first.next = second.next
            second.next = first
            prev = first 
            first = first.next
        self.head = dummy

        
        
