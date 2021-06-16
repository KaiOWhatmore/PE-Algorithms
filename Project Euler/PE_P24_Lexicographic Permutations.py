# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# for i in range(factorial(3) + 1):
#     print(i)

from itertools import permutations

perms = list(permutations('0123456789'))
mill = list(perms[999999])
solution = ''.join(mill)

print(solution)

# solution = ''.join(mill)
