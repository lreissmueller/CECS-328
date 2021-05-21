

def binary_search_01split(arr, key, lower_bound, upper_bound): # Binary Search Algorithm
    mid = int((upper_bound + lower_bound) / 2)
    if lower_bound > upper_bound:
        print(f"{key} not found.")
        return False
    if key == arr[mid] and arr[mid - 1] == 0:
        print(f"Found {arr[mid]} at index {mid}.")
        return True
    elif key == arr[mid] and arr[mid - 1] == 1:
        binary_search_01split(arr, key, lower_bound, mid - 1)
    elif key > arr[mid]:
        binary_search_01split(arr, key, mid + 1, upper_bound)
    elif key < arr[mid]:
        binary_search_01split(arr, key, lower_bound, mid - 1)


n = int(input("Array size: "))
k = int(input("Numbers equal to zero < array size: "))
arr = [0] * n
arr[k:] = [1] * (len(arr) - k)
print(arr, len(arr))

binary_search_01split(arr, 1, 0, n - 1)
