def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)
# This function has a time complexity of O(n^2 + n), which simplifies to O(n^2).
print_items(10)