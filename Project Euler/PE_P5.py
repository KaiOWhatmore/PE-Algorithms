# Smallest Mulitple
from functools import reduce


def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)


def LCM(a, b):
    return (a * b) / GCD(a, b)


# n = 2520

# for i in range(11):
#     print(GCD(i, 2520))
    # print(i, n)

# def small_mult(i, n):

nums = [x for x in range(1, 21)]

print(int(reduce(lambda x, y: LCM(x, y), nums)))
