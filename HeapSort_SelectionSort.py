import random
import math
import time

# PART A
# Create the following functions: build_MaxHeap, max_heapify, heap_sort.
def heapify(a, i, n):
    mx = i
    left = (2*i) + 1
    right = (2*i) + 2

    if left < n and a[left] > a[mx]:
        mx = left
    if right < n and a[right] > a[mx]:
        mx = right
    if mx != i:
        a[i], a[mx] = a[mx], a[i]
        return heapify(a, mx, n)


def build_heap(a):
    n = len(a)
    for i in range(n//2, -1, -1):
        heapify(a, i, n)


def heap_sort(a):
    n = len(a)
    build_heap(a)
    for i in range(n - 1, -1, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, 0, i)


def selection_sort(a):
    for k in range(len(a)):
        mn = k
        for i in range(k, len(a)):
            if a[i] < a[mn]:
                mn = i
        a[k], a[mn] = a[mn], a[k]


# Request the user to enter a positive integer, and call it n
n = int(input("Part A\nInput Size: "))
# Generate n random integers between -100 to 100 and save them in array a.
a = [0] * n

total_time = 0
repititions = 0

for i in range(100):
    for i in range(len(a)):
        a[i] = random.randint(-100, 100)
    start_time = time.time()
    heap_sort(a)  # Call heap_sort function to sort the array.
    end_time = time.time()
    total_time += abs(end_time - start_time)
    repititions += 1
average_time = total_time / repititions
print(f"Average time for HeapSort: {average_time} seconds.")
# Determine the average-running time of heap_sort function for n=1000, and 100 repetitions.

total_time = 0
repititions = 0

for i in range(100):
    for i in range(len(a)):
        a[i] = random.randint(-100, 100)
    start_time = time.time()
    selection_sort(a)
    end_time = time.time()
    total_time += abs(end_time - start_time)
    repititions += 1
average_time = total_time / repititions
print(f"Average time for SelectionSort: {average_time} seconds.\n\n")
# Compare your answer with the average-running time of selection sort (you need to implement it).


# --------------------------------------------------------------------------------------------------

# PART B
# Generate and print a random array of size 10.
a = [0] * 10
for i in range(len(a)):
    a[i] = round(random.random() * random.randint(-100, 100), 2)
heap_sort(a)
print(f"Part B\nResult: {a}")

