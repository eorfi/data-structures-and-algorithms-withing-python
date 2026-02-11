class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    ###########################
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for item in reversed(self.stack_list):
            print(item)
            
    def push(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
    def reverse_string(string):
        stack = Stack()
        reversed_str = ""
        for i in string:
            stack.push(i)
        while not stack.is_empty():
            reversed_str += stack.pop()
        return reversed_str
    
    def is_balanced_parentheses(parentheses):
        stack = Stack()
        for P in parentheses:
            if P == '(':
                stack.push(P)
            elif P == ')':
                if stack.is_empty() or stack.pop() != '(':
                    return False
        return stack.is_empty()
        
    def sort_stack(stack):
        additional_stack = Stack()

        while not stack.is_empty():
            temp = stack.pop()

            while not additional_stack.is_empty() and additional_stack.peek() > temp:
                stack.push(additional_stack.pop())

            additional_stack.push(temp)

        while not additional_stack.is_empty():
            stack.push(additional_stack.pop())
    
    class MyQueue:
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def enqueue(self, value):
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(value)

            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())

        def dequeue(self):
            if self.is_empty():
                return None
            return self.stack1.pop()

        def peek(self):
            return self.stack1[-1]
        
        def is_empty(self):
            return len(self.stack1) == 0
        
        


    
    
    


        