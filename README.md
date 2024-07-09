# W9D1 - Assignment - Big O notation

## Linear Search and Bubble Sort Algorithms

### 1. Linear Search Algorithm
The linear search algorithm is like looking for a favorite pair of socks in an unsorted laundry pile. We start at the top, check each one by one, and hope to find our match before we run out of socks. If we run out before finding a match, the sock has clearly disappeared into a negative space (-1). ;)

###     - Analysis and Optimization
#### Time Complexity: Linear search has a time complexity of 𝑂(𝑛), where 𝑛 = number of items in the array. We have to check each item once, which means worst-case scenario is our target is at the very end or not there at all.
#### Optimization: For linear search, I'm not aware of any optimizations that can improve efficiency. However, if we know our data might have duplicates and we only need to find the first occurrence, linear search is already optimal.
#### Trade-offs: Simple to visualize and use. No optimizations come to mind. (Reference: https://www.codecademy.com/resources/docs/general/algorithm - Linear time: If the time is proportional to the input size.The traverse of a list.)

### 2. Bubble Sort Algorithm
The bubble sort algorithm is like repeatedly comparing, in pairs, the filled amounts in a row of jars and swapping them if they're in the wrong order. We do this until no more swaps are needed, meaning our jars are finally sorted.

###     - Analysis and Optimization
#### Time Complexity: Bubble sort has a time complexity of 𝑂(𝑛^2) in the worst and average cases, where 𝑛 is the number of items in the array. This is because we usually need to make multiple passes over the entire array.
#### Optimization: An optimized version of bubble sort stops early if no swaps are made during a pass. This is because the array is already sorted. This optimization can reduce the number of passes in the best case to 𝑂(𝑛). In that case, however, the algorithm was better off not running in the first place...
#### Trade-offs: Easy to use and sort of easy to grasp the visualization, but inefficient for large arrays. Early stopping optimization can improve performance in best-case scenarios. (Reference: https://www.codecademy.com/resources/docs/general/algorithm/bubble-sort)
