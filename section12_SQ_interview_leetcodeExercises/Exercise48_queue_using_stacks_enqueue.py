# Queue Using Stacks: Enqueue ( ** Interview Question)
# You are given a class MyQueue that implements a queue using two stacks.
# Your task is to implement the enqueue method that should add an element to the back of the queue.
# To achieve this, you can use the two stacks stack1 and stack2.

# Initially, all elements are stored in stack1 and stack2 is empty.

# To add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.

# Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

# Your implementation should satisfy the following constraints:

# The method signature should be def enqueue(self, value).

# The method should add the element value to the back of the queue.
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    # def enqueue(self, value):
    #     # Move all elements from stack1 to stack2
    #     while self.stack1:
    #         self.stack2.append(self.stack1.pop())
        
    #     # Push the new element onto stack1
    #     self.stack1.append(value) 
        
    #     # Move all elements back from stack2 to stack1
    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())

    def enqueue(self, value): # enqueue means to add an element to the back of the queue
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value) # what is the usage of this line: it adds the new element to stack1, this new element will be at the bottom of stack1 after all elements are moved back from stack2 to stack1. value is the new element to be added to the queue and this value get get from the function parameter
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1) # add 1 to the queue
q.enqueue(2) # add 2 to the queue
q.enqueue(3) # add 3 to the queue

# Output the front of the queue
print("Front of the queue:", q.peek()) # should print 1 because 1 is the first element added to the queue

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
