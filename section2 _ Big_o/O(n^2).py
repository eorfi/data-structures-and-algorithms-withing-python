def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)

# This function has a time complexity of O(n^2) because it contains a nested loop.
# The outer loop runs n times, and for each iteration of the outer loop, the inner loop also runs n times.
# Therefore, the total number of iterations is n * n = n^2.
# This means that as n increases, the time taken by the function grows quadratically.
# The function prints pairs of indices (i, j) for all combinations of i and j from 0 to n-1.
# This is a classic example of a quadratic time complexity algorithm.
# The function is not optimized for performance and will take longer to execute as n increases.
# The function is useful for understanding how nested loops can lead to higher time complexities.
# It is important to be aware of this when designing algorithms, as O(n^2) can become impractical for large values of n.
# The function is a good example of how to analyze the time complexity of algorithms.
# It is also a reminder to consider alternative approaches, such as using hash tables or other data structures,
# which can often reduce the time complexity of certain problems.
# The function is straightforward and easy to understand, making it a good teaching tool for algorithm analysis.
# The function is not optimized for performance and will take longer to execute as n increases. 