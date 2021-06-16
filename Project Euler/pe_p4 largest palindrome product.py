# # Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

word = 'its our future'
wordreverse = 'its our future'[::-1]


def ispali(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


x = list(range(1, 1000))
y = list(range(1, 1000))

palis = []
pali_n = []

for i in x:
    for j in y:
        if ispali(i * j) is True:
            pali_n.append(i * j)
            if i * j < 10:
                break
            tuple((palis.append(i), palis.append(j)))


print(max(pali_n))


# def pairarray(array):
#     pairs = []

#     for i in range(1, len(array), 2):
#         pairs.append(list((array[i - 1], array[i])))

#     return pairs


# paired_palis = pairarray(palis)


# for i in range(0, len(paired_palis)):
#     double_pairs = paired_palis[i]
#     print(double_pairs)
#     multiply_sum = double_pairs[0] * double_pairs[1]
#     print(multiply_sum)
#     print()
