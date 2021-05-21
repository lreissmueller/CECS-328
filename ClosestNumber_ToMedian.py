import random

def median_of_three(arr, left, right):
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[mid], arr[left] = arr[left], arr[mid]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    if arr[right] < arr[left]:
        arr[right], arr[left] = arr[left], arr[right]
    return mid


def partition(arr, left, right):
    pi = median_of_three(arr, left, right)
    pv = arr[pi]
    end = right
    arr[right], arr[pi] = arr[pi], arr[right]
    right -= 1
    while left <= right:
        while arr[left] < pv:
            left += 1
            if left == right: break
        while arr[right] > pv:
            right -= 1
            if left == right: break
        if left >= right: break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    arr[left], arr[end] = arr[end], arr[left]
    return left


def quick_select(arr, left, right, k):
    while left < right:
        pi = partition(arr, left, right)
        if pi == k - 1:
            return pi
        elif pi < k - 1:
            left = pi + 1
        else:
            right = pi - 1
    return left + 1


def median_of_three_abs(arr, arr2, left, right):
    mid = (left + right) // 2
    if abs(arr[left]) > abs(arr[mid]):
        (arr[mid]), arr[left] = arr[left], arr[mid]
        (arr2[mid]), arr2[left] = arr2[left], arr2[mid]
    if abs(arr[mid]) > abs(arr[right]):
        arr[mid], arr[right] = arr[right], arr[mid]
        arr2[mid], arr2[right] = arr2[right], arr2[mid]
    if abs(arr[right]) < abs(arr[left]):
        arr[right], arr[left] = arr[left], arr[right]
        arr2[right], arr2[left] = arr2[left], arr2[right]
    return mid


def partition_abs(arr, arr2, left, right):
    pi = median_of_three_abs(arr, arr2, left, right)
    pv = arr[pi]
    end = right
    arr[right], arr[pi] = arr[pi], arr[right]
    arr2[right], arr2[pi] = arr2[pi], arr2[right]
    right -= 1
    while left <= right:
        while abs(arr[left]) < abs(pv):
            left += 1
            if left == right: break
        while abs(arr[right]) > abs(pv):
            right -= 1
            if left == right: break
        if left >= right: break
        arr[left], arr[right] = arr[right], arr[left]
        arr2[left], arr2[right] = arr2[right], arr2[left]
        left += 1
        right -= 1
    arr[left], arr[end] = arr[end], arr[left]
    arr2[left], arr2[end] = arr2[end], arr2[left]
    return left


def smallest_k_numbers(arr, arr2, left, right, k):
    while left < right:
        pi = partition_abs(arr, arr2, left, right)
        if pi == k - 1:
            return a[1:pi + 1]
        elif pi < k - 1:
            left = pi + 1
        else:
            right = pi - 1
    return a[1:left + 1]


print("\n1Q) Request the user to enter a positive integer, and call it n.")
n = int(input("1A) Size of array: "))
a = [0] * n
print()

print("2Q) Generate n random numbers between -100 to 100 and save them in a.")
for i in range(len(a)):
    a[i] = random.randint(-100, 100)
print(f"2A) {len(a)} Random elements generated...\n")

print("3Q) Print the generated array")
print(f"3A) a: {a}\n")

print(f"4Q) Request the user to enter a number between 1 to {n}, and call it K.")
k = int(input("4A) Number from 1 to n: "))
print()

print("5Q) Find the median of the array. O(n)")
median_i = quick_select(a, 0, n - 1, n // 2)
median = a[median_i]
print(f"5A) Median: {median}\n")

diff = [0] * n
print("6Q) Save the differences from the median (a[i]-median) in a new array and call it"
      "diff. (Question: What is the time complexity in this stage?  ----->")
print("Time Complexity of this^ operation: O(n)")
for i in range(len(diff)):
    diff[i] = abs(a[i] - median)
print(f"6A) Diff: {diff}\n")

print("7Q) Use diff to find the K closest numbers.")
diff = smallest_k_numbers(diff, a, 0, n - 1, k + 1)
print("7A) K closest numbers found...\n")

print("8Q) Shift the found K numbers back to their original value (+median). (Question: What is the time complexity "
      "in this step?)")
print("8A) This step is not needed, because both arrays are paired in the partitioning step."
      " However, this would be an O(n) operation.\n")

print("9Q) Print the answer :)")
print(f"9A) Median: {median}\n    Closest {k} Numbers: {diff}\n")

print("10Q) Calculate the total time complexity of your algorithm and present your answer when demoing.")
print("10A) The Worst Case: O(n^2)\n     The Average: O(n)")
