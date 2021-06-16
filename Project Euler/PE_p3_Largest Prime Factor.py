from math import isqrt


def isprime(n):
    for i in range(2, int((n)**(1 / 2)) + 1):
        if (n % i) == 0:
            return False
    else:
        return True


def square_limit(n):
    return int(n**(1 / 2) + 1)


def isfactor(n):
    factors = []
    for i in range(3, square_limit(n), 2):
        if n % i == 0:
            factors.append(i)
    return factors

#finding factors
def factors(n):
    factors = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    factors = list(set(factors))
    factors.sort()

    return factors


# Return Max Prime Factor

def primefactors(n):

    prime_array = []

    for i in isfactor(n):
        if isprime(i) is True:
            prime_array.append(i)

    return max(prime_array)


print(primefactors(600851475143))
