
# # def collatz(n):

# #     values = []

# #     while n > 1:

# #         values.append(n)

# #         if n % 2 == 0:
# #             n = n / 2
# #         else:
# #             n = 3 * n + 1

# #     return len(values + [n])


# # data = []
# # for i in range(1000000):
# #     data.append((collatz(i), i))


# # for j in data:

# #     max_val = j[1]

# #     print(max_val)


# # print(collatz(837799))


# # def collatz(n):
# #     it = 0
# #     if n == 1:
# #         return 1
# #     if n % 2 == 0:
# #         return collatz(n // 2) + 1
# #     else:
# #         return collatz(3 * n + 1) + 1


# # for i in range(1, 1000000):
# #     print(collatz(i))


# # dictionary with all the values initialized to 0
# dic = {n: 0 for n in range(1, 1000000)}

# # Entering the values of 1 and 2
# dic[1] = 1
# dic[2] = 2

# # for loop find find the size of collatz sequences
# for n in range(3, 1000000, 1):

#     # counter to count the size for each iteration
#     counter = 0

#     # original number
#     original_number = n

#     # while loop to do collatz iterations
#     while n > 1:

#         # check if the number is a previous sequence
#         if n < original_number:

#             # Size of collatz sequence for the iteration
#             dic[original_number] = dic[n] + counter
#             break

#         # collatz sequence conditions
#         if n % 2 == 0:
#             n = n / 2
#             counter += 1
#         else:
#             n = 3 * n + 1
#             counter += 1

# # dic.values() will give the values of the dictionary
# # list.index(some_number) will output the index
# # of the number. As the index starts from 0
# # we are adding one to the index.
# print(dic.values().index(max(dic.values())) + 1)

input('Enter a number:')
