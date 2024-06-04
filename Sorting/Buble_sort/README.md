# Time Complexity of Bubble Sort

Bubble sort employs two loops: an inner loop and an outer loop.

The inner loop performs O(n) comparisons deterministically.

# Worst Case

    In the worst-case scenario, the outer loop runs O(n) times.
    
    As a result, the worst-case time complexity of bubble sort is O(n x n) = (n^2).

# Best Case

    In the best-case scenario, the array is already sorted, but just in case, bubble sort performs O(n) comparisons.
    
    As a result, the time complexity of bubble sort in the best-case scenario is O(n).

# Average Case

    Bubble sort may require (n/2) passes and O(n) comparisons for each pass in the average case.
    
    As a result, the average case time complexity of bubble sort is O(n/2 x n) = O (n^2)
    
# Space Complexity -> O(1)
