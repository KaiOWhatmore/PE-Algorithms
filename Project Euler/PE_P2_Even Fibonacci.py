

fib_cache = {}

def fib(n):

    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        value = fib(n - 1) + fib(n - 2)

    # cache value
    fib_cache[n] = value
    return value


# In[388]:

for i in range(1,100):
    print(f'i:{i} || fib({i}); {fib(i)}')

# total = 0
# for i in range(1, 1000):

#     if fib(i) < int(4e6) and fib(i) % 2 == 0:
#         print(f'i:{i} | fib({i}); {fib(i)}')
#         total += fib(i)
#         print('total:', total)
