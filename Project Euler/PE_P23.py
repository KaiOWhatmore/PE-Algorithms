# def abundant_nums(n):
#     total = 1
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             total += i
#     return total > n


# arr = [i for i in range(12, 28124) if abundant_nums(i)]

# sum_arr = []
# for num1 in arr:
#     for num2 in arr:
#         sum_abunds = num1 + num2
#         if sum_abunds > 28123:
#             break
#         else:
#             sum_arr.append(sum_abunds)

# non_abunds = [x for x in range(28124) if x not in sum_arr]

# print(sum(non_abunds))
from math import sqrt


def divisors(n):
    divs = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    return list(set(divs))


# list to store the values of abundant numbers
ab = []

# For loop to generate the abundant numbers
for i in range(12, 28123):
    if sum(divisors(i)) > i:
        ab.append(i)

# first let us assume all the numbers are
# not sum of abundant numbers
non_ab_sum = [x for x in range(28123)]

# for loop to generate sum of two
# abundant numbers
for i in range(len(ab)):
    for j in range(i, 28123):
        if ab[i] + ab[j] < 28123:
            # negating the value of the abundant sum
            non_ab_sum[ab[i] + ab[j]] = 0
        else:
            break

# printing the value of the sum of non abundant sum
print(sum(non_ab_sum))
