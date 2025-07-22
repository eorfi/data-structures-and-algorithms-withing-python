# the o(log n) is the time complexity of this function because it uses a binary search algorithm to find an item in a sorted list.
def binary_search(arr, target): 
    left, right = 0, len(arr) - 1 # initialize the left and right pointers
    # while loop to narrow down the search space    
    
    while left <= right:
        mid = (left + right) // 2 # find the middle index
        
        if arr[mid] == target: # if the middle element is the target
            return mid
        elif arr[mid] < target: # if the middle element is less than the target
            # move the left pointer to the right of mid
            left = mid + 1
        else: # if the middle element is greater than the target
            right = mid - 1 # move the right pointer to the left of mid
            
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(my_list, 8)
if result != -1:
    print(f"Element found at index: {result}")