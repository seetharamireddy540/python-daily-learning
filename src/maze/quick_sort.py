def quicksort(arr):# -> Any:
    # If the list has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Create three lists:
    # - Left: elements smaller than pivot
    # - Middle: elements equal to pivot
    # - Right: elements larger than pivot
    tmp = []
    for x in arr:
        if x < pivot:
            tmp.append(x)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right lists
    # Combine the sorted lists
    return quicksortd(left) + [pivot] + quicksort(right)

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quicksort(numbers)
print("Sorted array:", sorted_numbers)