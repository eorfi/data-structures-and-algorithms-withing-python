# HT: Group Anagrams ( ** Interview Question)
# You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

# For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

# You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.

# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################

# def group_anagrams(strings):
#     # create an empty hash table
#     anagram_groups = {}

#     # iterate through each string in the array
#     for string in strings:
#         # sort each string to get its canonical form
#         # sorted('eat') returns ['a', 'e', 't']
#         # ''.join(['a', 'e', 't']) coverts the array of chars to 'aet' string
#         canonical = ''.join(sorted(string))
#         # this line above is put together to create a string that represents the sorted version of the original string
#         # sorted() function returns a list of characters in sorted order
#         # ''.join() is used to concatenate the list into a single string
#         # this is the canonical form of the string
#         # the output of this line for 'eat', 'tea', and 'ate' will all be 'aet'

 
#         # check to see if the canonical form of the string exists in the hash table
#         # how this line can check if canonical or not?
#         # it checks if the sorted version of the string is already a key in the dictionary

#         if canonical in anagram_groups:
#             # if it does then add the string there
#             anagram_groups[canonical].append(string)
#         else:
#             # otherwise create new canonical form and add the string there
# #             anagram_groups[canonical] = [string]

# #         Example with ["eat", "tea", "tan", "ate", "nat", "bat"]:
# # "eat" → canonical = "aet" → NEW → {"aet": ["eat"]}

# # "tea" → canonical = "aet" → EXISTS → {"aet": ["eat", "tea"]}

# # "tan" → canonical = "ant" → NEW → {"aet": ["eat", "tea"], "ant": ["tan"]}

# # "ate" → canonical = "aet" → EXISTS → {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}

# # "nat" → canonical = "ant" → EXISTS → {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}

# # "bat" → canonical = "abt" → NEW → {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}
 
#     # convert the hash table to a list of lists
#     return list(anagram_groups.values())

# def group_anagrams(strings):
#     # anagram_groups = {}
#     # for string in strings:
#     #     canonical = ''.join(sorted(string))
#     #     if canonical in anagram_groups:
#     #         anagram_groups[canonical].append(string)
#     #     else:
#     #         anagram_groups[canonical] = [string]
#     # return list(anagram_groups.values())

# def group_anagrams(strings):
#     anagram_groups = {}
#     for string in strings:
#         canonical = ''.join(sorted(string))
#         if canonical in anagram_groups:
#             anagram_groups[canonical].append(string)
#         else:
#             anagram_groups[canonical] = [string]
#     return list(anagram_groups.values())

# def group_anagrams(strings):
#     anagram_groups = {}
#     for string in strings:
#         canonical = ''.join(sorted(string))
#         if canonical in anagram_groups:
#             anagram_groups[canonical].append(string)
#         else:
#             anagram_groups[canonical] = [string]
#     return list(anagram_groups.values)

# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################


def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        # Sort the string to create a key
        key = ''.join(sorted(string))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return list(anagrams.values())

    

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""