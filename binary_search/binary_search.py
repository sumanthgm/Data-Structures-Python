"""Iterative binary search on a sorted list."""


def binary_search(key, arr):
    """Return the index of key in sorted arr, or -1 if absent."""
    low, high = 0, len(arr) - 1  # was len(arr) // 2, which missed keys in the upper half
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    key = int(input("Enter key: "))
    print("Index:", binary_search(key, nums))
