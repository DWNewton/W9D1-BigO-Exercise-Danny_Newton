def linear_search(arr, target):
    """
    Search for target in array like we're hunting for buried treasure.
    Return index of first occurrence, or -1 if treasure is not found.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def bubble_sort(arr):
    """
    Sort array by bubbling largest element to the end, like bubbles rising to the surface.
    """
    n = len(arr)
    '''
        Based on pseudocode provided by https://www.codecademy.com/resources/docs/general/algorithm/bubble-sort :
        Algorithm: BubbleSort(Array)
    for i from 0 to Array.length - 1
        set swapped to false
        for j from 0 to Array.length - i - 1
            if Array[j] > Array[j + 1]
                swap Array[j] and Array[j + 1]
                set swapped to true
        if not swapped
            break // Array is sorted
        '''
    for i in range(n):
        # Track if we made any swaps this pass; if not, we're done early!
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Linear Search Sample Test Cases
arr = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(arr, target)}")  # Output: 3
target = 11
print(f"Index of {target}: {linear_search(arr, target)}")  # Output: 4
target = 99
print(f"Index of {target}: {linear_search(arr, target)}")  # Output: -1

# Bubble Sort Sample Test Cases
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(arr)}")  # Output: [11, 12, 22, 25, 34, 64, 90]
arr = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(arr)}")  # Output: [1, 2, 4, 5, 8]