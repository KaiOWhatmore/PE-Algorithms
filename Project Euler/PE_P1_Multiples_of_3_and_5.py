number = range(0, 1000)
array = []
total = 0

for i in number:
    if i % 3 == 0 or i % 5 == 0:
        array += [i]
        total += i

print(total)
