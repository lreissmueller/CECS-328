import random
import time
import numpy as np


def binary_search(arr, key, lower_bound, upper_bound): # Binary Search Algorithm
    mid = int((upper_bound + lower_bound) / 2)
    if lower_bound > upper_bound:
        # print(f"{key} not found.")
        return False
    if key == arr[mid]:
        # print(f"Found {arr[mid]} at index {mid}.")
        return True
    elif key > arr[mid]:
        binary_search(arr, key, mid + 1, upper_bound)
    elif key < arr[mid]:
        binary_search(arr, key, lower_bound, mid - 1)


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            # print(f"Found {arr[i]} at index {i}.")
            return True
    # print(f"{key} not found.")
    return False


n = int(input("Enter an array size: "))  # REQUEST THE USER TO ENTER A POSITIVE INTEGER, AND CALL IT n. (n = 10^5)
a = []
for i in range(n):  # Generate n random integers between -1000 to 1000 and save them in an array a.
    a.append(random.randint(-1000, 1000))
a.sort()  # Sort a(you can use any sorting algorithm you want.)

print("\n(PART A)")  # PART A


iterations = 100
# BS
# print("Binary Search:")
bs_start = time.time()
for i in range(iterations):
    key = a[random.randint(0, n - 1)]  # Pick a random number in a and save it in a variable key
    binary_search(a, key, 0, len(a) - 1)  # Call each function separately to search for the key in a given array.
bs_end = time.time()
bs_total_time = abs(bs_start - bs_end)
bs_average_time = bs_total_time / iterations  # To calculate the average-running time, you need to have a
# timer to save the total runtime when repeating step 4 and 5 for 100 times.

# LS
# print("Linear Search:")
ls_start = time.time()
for i in range(iterations):  # Refer to above comments
    key = a[random.randint(0, n - 1)]
    linear_search(a, key)
ls_end = time.time()
ls_total_time = abs(ls_start - ls_end)
ls_average_time = ls_total_time / iterations

print(f"\nTotal time for Binary Search: {bs_total_time}.\nAverage time for Binary Search: {bs_average_time} seconds.")
print(f"Total time for Linear Search: {ls_total_time}.\nAverage time for Linear Search: {ls_average_time} seconds.")


print("\n\n(PART B)")  # PART B
# BS
# print("Binary Search:")
bs_start = time.time()  # Repeat steps 1-3 in PART A.
key = 5000  # To have the worst-case scenario, set the value of the key to 5000 to make sure it does not
# exist in the array.
binary_search(a, key, 0, len(a) - 1)  # Run each functions only once.
bs_end = time.time()
bs_total_time = abs(bs_start - bs_end)
bs_average_time = bs_total_time

# LS
# print("Linear Search:")
ls_start = time.time()
# Refer to above comments
key = 5000
linear_search(a, key)
ls_end = time.time()
ls_total_time = abs(ls_start - ls_end)
ls_average_time = ls_total_time
bs_one_line = bs_total_time / (5 * np.log(n))

print(f"\nWorst case for Binary Search: {bs_total_time} seconds.")  # Worst case.
print(f"Worst case for Linear Search: {ls_total_time} seconds.")
print(f"Time it takes to run one line in Binary Search: {bs_one_line} seconds")  # One line running time.
print(f"Worst case running time for Binary Search = O(log(n)) when n = 10^15 = {bs_one_line * np.log(10**15)} seconds.")  # Worst case for n = 10^15.

# Explain parts 4 and 5 in words.
print(f"""
In part 4, I calculated the time it takes to run one single line using binary search by taking the total time it takes
find an element in an array of 10^6(my computer was too fast for 100,000) elements, and divided it by the total amount
lines ran. In this case, since the time complexity is observantly = O(log(n)) (array is continuously halved), the total
lines ran is log(10^5). This means that the time it takes to run one line is very small.

Part 5 piggy-backed off of this idea, but multiplying the time it takes to run a single line by the amount of lines, which
would be log(10^15).


""")

print("(PART C)")  # PART C
# Given a sorted array with n integers, provide an algorithm with the running time of O(logn) that
# checks if there is an i for which a[i]= i.


def binary_search_for_i(arr, lower_bound, upper_bound):  # Binary Search Algorithm to find if a[i] == i
    mid = int((upper_bound + lower_bound) / 2)
    if lower_bound > upper_bound:
        print(f"False! {mid} not equal to {arr[mid]}.")
        return False
    if mid == arr[mid]:
        print(f"True! Found {arr[mid]} at index {mid}.")
        return True
    elif mid > arr[mid]:
        binary_search_for_i(arr, mid + 1, upper_bound)
    elif mid < arr[mid]:
        binary_search_for_i(arr, lower_bound, mid - 1)


a = [1, 1.5, 2, 5, 10, 21]
a.sort()
binary_search_for_i(a, 0, len(a) - 1)
a = [1, 5, 12, 17, 19, 27]
a.sort()
binary_search_for_i(a, 0, len(a) - 1)
