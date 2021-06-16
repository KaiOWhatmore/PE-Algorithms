from math import sqrt


# print(sqrt(4))

# calculate prime number


def prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


for i in range(10):
    print(i, prime(i))
# create an array of prime numbers -1000 to 1000:
prime_arr = [1]
for i in range(2, 1001):
    if prime(i) == True:
        prime_arr.append(i)

negatives = [x * -1 for x in prime_arr]

ab = negatives + prime_arr


def euler_quad(n): return n**2 + n + 41


def quad_80(n): return n**2 - 79 * n + 1601

# calculate the number of prime numbers in the quadratic


def f(n): return n**2 - 4 * n + 11


def prime_terms(f_n):
    count = 0
    while prime(f_n(count)) == True:
        count += 1
    return count


def nmax(a, b):
    num1 = (-a + sqrt(a**2 - 4 * (b - 1601))) / 2
    num2 = (-a - sqrt(a**2 - 4 * (b - 1601))) / 2

    # if num1 % 1 == 0 and num2 % 1 == 0:
    return [num1, num2]


values = []
n = 0
for i in range(len(ab)):
    for j in range(i):
        x = nmax(ab[i], ab[j])
        if x is not None:

            if ab[j] > 0:
                values.append([int(x[0]), [ab[i], ab[j]]])


print((values))

# print(ab)

# for i in range(3)
