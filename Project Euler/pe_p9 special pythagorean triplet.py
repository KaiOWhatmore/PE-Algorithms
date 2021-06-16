# The solution. lol.

def a(n, m):
    return m**2 - n**2


def b(n, m):
    return 2 * m * n


def c(n, m):
    return m**2 + n**2

def pythag_triplet():

    for m in range(1, 32):

        for n in range(1, m):

            if a(n, m) + b(n, m) + c(n, m) == 1000:

                return a(n, m) * b(n, m) * c(n, m), a(n, m), b(n, m), c(n, m)


# In[245]:


print(pythag_triplet())
