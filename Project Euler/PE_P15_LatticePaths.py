# # Problem 15: Lattice paths, *Permutations*

# # Permutations of Binary Bits
# There are two options: right and down which is the same as 1 (right) and 0 (down)
# we then have a sequence of 1s and 0s that is equivalent to a permutation
# this problem is then based on understanding the amount of permutations which is:
# where n is the amount of strings and n/2 is the amount of 1s
# Python program to demonstrate infinite iterators:
# *itertools is a superior version for faster iterations*

# In[421]:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def permutations(n):
    return int(factorial(n * 2) / factorial(n)**2)
    # return (2/factorial(n))

print(permutations(4))
