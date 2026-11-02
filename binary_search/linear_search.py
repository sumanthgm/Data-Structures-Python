"""Linear search."""


def linear_search(arr, key):
    """Return the index of the first occurrence of key in arr, or -1."""
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    key = int(input("Enter the key to search: "))
    print(linear_search(arr, key))
