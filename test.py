# def first_n(n):
#     '''Build and return a list'''
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums
#
#
# sum_of_first_n = sum(first_n(1000000))
# print(sum_of_first_n)

# print(2 * n for n in range(50))

# def numbers_gen():
#     yield 1
#     yield 2
#     yield 3
#
# gen = numbers_gen()
# print(gen)

# def custom_gen(n):
#     for i in range(n):
#         yield i
#
# g = custom_gen(3)
#
# for num in g:
#     print(num)

#Countdown generator:

# def countdown(n):
#     while n >= 1:
#         yield n
#         n -= 1
#
#
# for c in countdown(5):
#     print(c)

#
# def read_file_lines(filename):
#     with open(filename, 'r') as file:
#         contents = file.readline()
#         while contents != "":
#             yield contents
#             contents = file.readline()
#
#
# for line in read_file_lines("textfile.txt"):
#     print(line)

from word_frequency_counter import WordFrequency

test = WordFrequency("textfile.txt")
print(test.get_freq_dict())
print(test.get_sorted_freq_dict())