from math import sqrt
from random import randint

def sums():
    total = 0
    number = ''
    nums = []

    for i in range(4):
        n = randint(0,9)
        total += n**4
        number += str(n)

    if number != str(total):
        return True, number
    print(number)
#
i = 0
nums = []
while True:
    i+=1

    if i > 10:
        break

    nums.append(sums())

print(nums)



# i = 0
# while True:
#     i+=1
#     print(i)
#
#     if i >= 10:
#         break
