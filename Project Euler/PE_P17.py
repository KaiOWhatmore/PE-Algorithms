# Numbers 1-10
one, two, three, four, five, six, seven, eight, nine = [
    3, 3, 5, 4, 4, 3, 5, 5, 4]
ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]

# Teens
eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen = [
    6, 6, 8, 8, 7, 7, 9, 8, 8]
teens = [6, 6, 8, 8, 7, 7, 9, 8, 8]

# Tens
# ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety = [3,
#                                                                      6, 6, 5, 5, 5, 7, 6, 6]
tens = [6, 6, 5, 5, 5, 7, 6, 6]


# hundreds
onehundred, twohundred, threehundred, fourhundred, fivehundred, sixhundred, sevenhundred, eighthundred, ninehundred = [
    10, 10, 12, 11, 11, 10, 12, 12, 11]
hundreds = [10, 10, 12, 11, 11, 10, 12, 12, 11]

onethousand = 11

con = 3

# sum of 1-10:
sum(ones)
sum(teens)

# numbers 1-99
totes = 0
for ten in tens:
    for one in ones:
        totes += ten + one

# update ten to 3
ten = 3

totes += sum(ones) + ten + sum(teens) + sum(tens)
print(totes)

"""numbers 100-900"""

# sum of 100,200, ... ,900
totes += sum(hundreds)

# sum of 101,102,103, ... 201,202,203, ... 901,902,909
for hundred in hundreds:
    for one in ones:
        totes += hundred + one + con

# sum of 110, 210, 310, ... , 910
for hundred in hundreds:
    totes += hundred + con + ten

# sum of 120,130, ... 320,330, ... , 920,990
for hundred in hundreds:
    for ten in tens:
        totes += hundred + ten + con

# sum of 121,122,123, ... , 321,322,323, ... , 921,922,923
for hundred in hundreds:
    for ten in tens:
        for one in ones:
            totes += hundred + ten + one + con

# sum of 111,112,113, ... , 911,912,913
for hundred in hundreds:
    for teen in teens:
        totes += hundred + teen + con

# one thousand:
totes += onethousand


print(totes)
