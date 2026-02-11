# Set: Has Unique Chars ( ** Interview Question)
# Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

# WRITE HAS_UNIQUE_CHARS FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
def has_unique_chars(input_string):
    # create an empty set to store unique characters
    char_set = set()
    
    # iterate through each character in the input string
    for char in input_string:
        # if the character is already in the set, return False
        if char in char_set:
            return False
        # otherwise, add the character to the set
        char_set.add(char)
    
    # if all characters are unique, return True
    return True



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""