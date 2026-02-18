# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
# def find_longest_string(my_list):
#     if not my_list:
#         return ""
#     long_str = my_list[0]
#     for i in range(len(my_list)):
#         if len(my_list[i]) > len(long_str):
#             long_str = my_list[i]
#     return long_str


def find_longest_string(string_list):
    longest_string = ""
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)