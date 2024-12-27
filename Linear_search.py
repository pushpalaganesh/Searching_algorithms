def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
target = int(input("Enter the target integer: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the list")
