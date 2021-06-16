def trianglenumbers(n):
    tri = 0
    for i in range(n + 1):
        tri += i

    return tri


# In[191]:


def divisors(n):
    numbers = []

    for num in range(1, n + 1):
        if n % num == 0:
            numbers.append(num)

    return len(numbers)


# In[254]:


def trinumslist(n):

    values = []

    for i in range(1, n + 1):

        values.append((divisors(trianglenumbers(i)), trianglenumbers(i)))
    maxdiv = max(values)[0]
    return values, maxdiv
    # return values
    # return trianglenumbers(i), divisors(trianglenumbers(i))
    # print('n',i,'|','trivalue:',trianglenumbers(i),'|','no_of_divisors:',divisors(trianglenumbers(i)))


# In[297]:


def trinumslist(n):

    values = []

    for i in range(1, n + 1):
        if divisors(trianglenumbers(i + 1) > divisors(trianglenumbers(i))):
            [divisors(trianglenumbers(i + 1)), trianglenumbers(i + 1)] = [divisors(trianglenumbers(i)), trianglenumbers(i)]

    # maxdiv = max(values)[0]
    return [divisors(trianglenumbers(i + 1)), trianglenumbers(i + 1)]


# In[289]:


def maxdivisor(n):
    i = 1
    while max(trinumslist(i))[0] < n:
        trinumslist(i)

        i += 1
    return trinumslist(i)
