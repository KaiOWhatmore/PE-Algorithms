num = 1
den = 7


def recurring_nums(num, den):
    rems = ''

    rem = num % den
    rem_dic = {}

    while (rem != 0) and (rem not in rem_dic):

        rem_dic[rem] = len(rems)
        # print(len(rems), rem, rem_dic)

        # Step 1: remainder x 10
        rem *= 10

        # Step 2: decimal = remainder x 10 // denominator

        rem1 = rem // den
        # convert to string to concatenate
        rems += str(rem1)

        # Step 3: remainder mod denominator to update loop
        rem = rem % den

    if rem == 0:
        return None
    else:
        return rems


# recurring_nums(1, 3)

recur_arr = {}
length = []
for i in (range(2, 1000)):
    if recurring_nums(1, i) is not None:
        # recur_arr[recurring_nums(1, i)] = len(recurring_nums(1, i))
        length.append((len(recurring_nums(1, i)), i))

# print((recur_arr))
length.sort()
print(max(length))
