import random


def median_of_three(arr, left, right):
    mid = (right + left) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    return mid


def partition(arr, left, right):
    pivot_index = median_of_three(arr, left, right)
    pivot_value = arr[pivot_index]
    end = right
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    right -= 1
    while left <= right:
        while arr[left] < pivot_value:
            left += 1
            if left == right: break
        while arr[right] > pivot_value:
            right -= 1
            if left == right: break
        if left >= right: break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    arr[end], arr[left] = arr[left], arr[end]
    return left


def quick_select(arr, k, left, right):
    while left < right:
        p_i = partition(arr, left, right)
        if k - 1 == p_i:
            return arr[k - 1]
        elif k - 1 < p_i:
            right = p_i - 1
        else:
            left = p_i + 1
    return arr[left]

def max_k(arr, k, left, right):
    end = right
    k = len(arr) - k
    while left < right:
        p_i = partition(arr, left, right)
        if k - 1 == p_i:
            return arr[k: end + 1]
        elif k - 1 < p_i:
            right = p_i - 1
        else:
            left = p_i + 1
    return arr[k: end + 1]


print(f"\n----------(PART A)----------\n\n")
n = int(input("Array size:"))  # PART A
a = []
for i in range(n):
    a.append(random.randint(-100, 100))
print(a)
k = int(input(f"Enter a Kth least element between 1 and {n}: "))
print(f"K: {k}\n{k}th Least Element: {quick_select(a,k,0,len(a)- 1)}\nArray: {a}")


print(f"\n----------(PART B)----------\n\n")
n = int(input("Array size:"))  # PART B
arr = [0] * n
for i in range(n):
    arr[i] = random.randint(-100, 100)
print(arr)
k = int(input("Max K numbers: "))
print(f"Max {k} numbers: {max_k(arr, k, 0, len(arr) - 1)}\nArray: {arr}")
