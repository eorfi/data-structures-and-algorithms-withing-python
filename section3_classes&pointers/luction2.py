# class Cookie:
#     def __init__(self, color):
#         self.color = color
    
#     def get_color(self):
#         return self.color
    
#     def set_color(self):
#         self.color = color
    
# cooki_one = Cookie('green')
# cooki_two = Cookie('blue')

# cooki_two.set_color('red')

# print('Cookie one is ', cooki_one.get_color())
# print("Cookir two is ", cooki_two.get_color())

# class LinkedList:
#     def __init__(self, value):
#     def append (self, value):
#     def pop(self):
#     def prepend(self, value):
#     def insert(self, index, value):
#     def remove(self, value):

################################################

# pointers 

'''
# Understanding Pointers

## What are Pointers?

Pointers are variables that store memory addresses rather than actual values. They "point to" locations in memory where data is stored. Pointers are fundamental in low-level programming languages like C and C++ because they provide direct memory access and manipulation.

## How Pointers Work

1. **Declaration**: You declare a pointer with a specific data type (int*, char*, etc.)
2. **Initialization**: You assign it the address of another variable using the address-of operator (&)
3. **Dereferencing**: You access the value at the memory address using the dereference operator (*)

## Pointers in Python

**Python doesn't have explicit pointers like C/C++**, but it uses references behind the scenes. Everything in Python is an object, and variables are references to these objects. This is similar to pointers but with automatic memory management (garbage collection).

### Python's Reference System (Similar to Pointers)

1. **Variables are references**: When you assign a variable, you're creating a reference to an object
2. **Mutable vs Immutable**: Behavior differs between mutable (lists, dicts) and immutable (ints, strings, tuples) objects
3. **id() function**: Returns the memory address of an object (similar to getting a pointer's address)

## Examples in Python

### Example 1: Basic reference behavior
```python
a = 10
b = a  # b references the same object as a
print(id(a), id(b))  # Both will show the same memory address

a = 20  # Now a references a new object
print(a, b)  # Output: 20 10
```

### Example 2: Mutable objects (like pointers)
```python
list1 = [1, 2, 3]
list2 = list1  # Both reference the same list object

list2[0] = 99
print(list1)  # Output: [99, 2, 3] - both changed
```

### Example 3: Function arguments (pass by object reference)
```python
def modify_list(lst):
    lst.append(4)  # Modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```

### Example 4: Simulating pointers with ctypes (advanced)
```python
import ctypes

# Simulating pointers using ctypes
x = ctypes.c_int(10)  # Create a C-like integer
px = ctypes.pointer(x)  # Create a pointer to x

print(px.contents)  # Access the value: c_int(10)
px.contents.value = 20  # Modify through pointer
print(x.value)  # Now 20
```

## Key Differences from C/C++ Pointers

1. No pointer arithmetic in Python
2. No need to manually allocate/deallocate memory
3. References are automatically managed by Python's garbage collector
4. You can't directly access arbitrary memory locations

While Python doesn't have traditional pointers, understanding how references work in Python is crucial for writing efficient code, especially when dealing with mutable objects.
'''

# Understanding Pointers in Python
num1 = 11
num2 = num1  # num2 references the same object as num1

print("Before num2 value is updated:")
print("num1:", num1, "num2:", num2)
print("/nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) # Both will show the same memory address

num2 = 22  # Now num2 references a new object
print("\nAfter num2 value is updated:")
print("num1:", num1, "num2:", num2)
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))  # Now they point to different addresses

# num 1 = num2 + 1 # num1 now references a new object

dict1 = {'a': 1, 'b': 2}

dict2 = dict1  # dict2 references the same dictionary object as dict1
print("\nBefore dict2 is modified:")
print("dict1:", dict1, "dict2:", dict2)
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))  # Both will show the same memory address

dict2['a'] = 3  # Modifying dict2 also modifies dict1
print("\nAfter dict2 is modified:")
print("dict1:", dict1, "dict2:", dict2)
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))  # Still the same address

