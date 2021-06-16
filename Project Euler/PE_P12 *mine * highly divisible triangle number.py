from math import isqrt

import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())


def divisors(n):
    count = 0
    for i in range(1, isqrt(n) + 1):

        if n % i == 0:
            count += 2
    return count


def tri_nums(n):
    if n == 1:
        return 1
    else:
        return tri_nums(n - 1) + n


n = 0
while True:
    n += 1
    print(tri_nums(n), divisors(tri_nums(n)), n)

    if divisors(tri_nums(n)) > 500:
        print(tri_nums(n))
        break


# def tri_nums(num):
#     total = 0
#     trinums = []
#     for index, n in enumerate(range(1, num + 1)):
#         total += n
#     return total
