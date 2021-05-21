import random

def bs_smallest_missing(a, lower, upper):
    mid = int((upper + lower) / 2)
    if a[upper] == upper:
        print(upper + 1)
        return upper + 1
    if lower >= upper:
        print(f"Lowest missing value is {mid}")
        return mid
    elif (a[mid] > mid) & (a[mid - 1] == mid - 1):
        print(f"Lowest missing value is {mid}")
        return mid
    elif a[mid] > mid:
        bs_smallest_missing(a, lower, mid - 1)
    elif a[mid] == mid:
        bs_smallest_missing(a, mid + 1, upper)


m = int(input("Range of numbers in array: "))
n = int(input("Size of array: "))
a = []
while len(a) < n:
    r = random.randint(0, m)
    if r not in a:
        a.append(r)
a.sort()
print(a)
bs_smallest_missing(a, 0, len(a) - 1)
