import random

def binary_search_sqrt(lower, upper, n):

    mid = int((upper + lower) / 2)
    print(mid)
    if mid*mid == n:
        print(f"{mid} is sqrt({n}).")
        return mid
    elif (mid*mid > n) & ((mid - 1)**2 < n):
        print(f"{mid} i sqrt({n}).")
        return mid
    elif mid*mid < n & (mid + 1)**2 > n:
        print(f"{mid + 1} s sqrt({n}).")
        return mid + 1
    elif mid*mid > n:
        binary_search_sqrt(lower, mid - 1, n)
    elif mid*mid < n:
        binary_search_sqrt(mid + 1, upper, n)


n = int(input("Number: "))
binary_search_sqrt(0, n, n)

