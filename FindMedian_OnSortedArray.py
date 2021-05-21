import random


def bs_median_sorted(a1, a2, l1, u1, l2, u2):  # Binary Search Algorithm
    print(a1[l1:u1+1],a2[l2:u2+1])
    if u1 - l1 <= 1:
        print((max(a1[l1], a2[l2]) + min(a1[u1], a2[u2])) / 2)
        exit()

    mid1 = int((u1 + l1) / 2)
    mid2 = int((u2 + l2) / 2)
    even = True if (u1 - l1 + 1) % 2 == 0 else False

    if even:
        m1 = (a1[mid1] + a1[mid1 + 1]) / 2
        m2 = (a2[mid2] + a2[mid2 + 1]) / 2
    else:
        m1 = a1[mid1]
        m2 = a2[mid2]

    if m1 == m2:
        print(m1)
        exit()

    if even and m1 < m2:
        bs_median_sorted(a1, a2, mid1 + 1, u1, l2, mid2)
    elif even and m1 > m2:
        bs_median_sorted(a1, a2, l1, mid1, mid2 + 1, u2)

    if m1 < m2:
        bs_median_sorted(a1, a2, mid1, u1, l2, mid2)
    else:
        bs_median_sorted(a1, a2, l1, mid1, mid2, u2)


n = int(input("Array size: "))
a1 = [0] * n
for i in range(n):
    a1[i] = random.randint(0, 50)
a2 = [0] * n
for i in range(n):
    a2[i] = random.randint(0, 50)
a1.sort()
a2.sort()
print(a1, a2)
bs_median_sorted(a1, a2, 0, n - 1, 0, n - 1)







