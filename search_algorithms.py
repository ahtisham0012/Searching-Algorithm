def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


def linear_search(arr, target):
        steps = 0

    for index, element in enumerate(arr):
        steps += 1
        if element == target:
            return index, steps

    return -1, steps


if __name__ == "__main__":
    print("Enter the sorted array (comma-separated):")
    array = list(map(int, input().split(",")))

    print("Enter the target value:")
    target_value = int(input())

    # Perform Binary Search
    binary_result, binary_steps = binary_search(array, target_value)
    if binary_result != -1:
        print(f"Binary Search: Target found at index {binary_result} in {binary_steps} steps.")
    else:
        print(f"Binary Search: Target not found after {binary_steps} steps.")

    # Perform Linear Search
    linear_result, linear_steps = linear_search(array, target_value)
    if linear_result != -1:
        print(f"Linear Search: Target found at index {linear_result} in {linear_steps} steps.")
    else:
        print(f"Linear Search: Target not found after {linear_steps} steps.")
