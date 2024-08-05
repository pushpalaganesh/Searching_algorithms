def Binary_Search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Get user input
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Sort the array to ensure it is in ascending order
arr.sort()
print("The sorted list is: ",arr)
target = int(input("Enter the target integer: "))

# Perform binary search
result = Binary_Search(arr, target)

# Output the result
if result != -1:
    print(f"Element found at index {result} in the sorted array")
else:
    print("Element not found in the array")
