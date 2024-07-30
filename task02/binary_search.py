def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)

# Test the function
arr = [0.9, 1.22, 1.3, 2.4, 3.5, 5.6, 7.9, 9.9, 8.2]
target = 3.0
result = binary_search(arr, target)
print(result)