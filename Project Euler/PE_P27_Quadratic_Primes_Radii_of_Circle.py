from math import isqrt


def sieve(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return [i for i in range(n) if is_prime[i]]


def isprime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, isqrt(abs(n)) + 1):
        if n % i == 0:
            return False
    return True


primes1000 = sieve(1000)

# must use slice method to ensure the loop doesn't extend to infinity
primes1000_v2 = primes1000[:]

largest = 0

for b in primes1000:
    for a in primes1000:
        i = 0
        while True:

            quadratic = i**2 + a * i + b
            if quadratic not in primes1000_v2:
                if isprime(quadratic):
                    primes1000_v2.append(quadratic)
                else:
                    if i - 1 > largest:
                        largest = i - 1
                        axb = a * b
                    break
            i += 1

        i = 0
        while True:
            quadratic = i**2 - a * i + b
            if quadratic not in primes1000_v2:
                if isprime(quadratic) and quadratic > 0:
                    primes1000_v2.append(quadratic)
                else:
                    if i - 1 > largest:
                        largest = i - 1
                        axb = -1 * a * b
                    break
            i += 1

print(axb)


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = list1[:]

# for i in list1:
#     list2.append(i)
#     print(list1)

print(list1)
print(list2)
