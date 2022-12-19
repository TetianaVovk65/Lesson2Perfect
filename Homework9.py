import random
from typing import List

#task1
file = open('data.txt', 'r')
lines = 0
numbers = 0
for line in file:
    lines += 1
    numbers += line.isdigit()
file_numbers = open('text1.txt', 'w')
file.write(numbers)
file.close()



# # task2 -good
# text = input('Enter text: ')
# file = open('data.txt', 'w')
# file.write(text)
# file.close()

task3
ask_number = int(input('Write number:'))
for i in range(ask_number):
    number = int(input(f'Enter number {i} ='))
    file = open('numbers.txt', 'w')
    file.write(str(number) + '\n')

# file.close()

# #task4
# unique_random_numbers = {random.randint(1, 100) for _ in range(100)}
# print(unique_random_numbers)
# for i in range(unique_random_numbers):
#     number = int(input(f'Enter number {i} ='))
# file = open('random_numbers.txt', 'w')
# file.writelines(str(unique_random_numbers) + '\n')

# #task5 - good
# file = open('text1.txt')
# lines = 0
# words = 0
# for line in file:
#     lines += 1
#     words += len(line.split())
# print("Words:", words)

#task6 -cant add the last number
# file = open('text2.txt')
# a = (file.readline())
# b = ''
# while a:
#     b = b + a
#     a = file.readline()
# b = b.split(' ')
# result = 0
# for i in b:
#     if i.isdigit():
#         result = result + int(i)
# print(result)

# #task7 -good
# file = open('text3.txt')
# file_read = (file.readline())
# lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']
# lst = []
#
# for word in file_read.lower().split():
#     if not word in lst_no:
#         _word = word
#         if word[-1] in lst_no:
#             _word = _word[:-1]
#         if word[0] in lst_no:
#             _word = _word[1:]
#         lst.append(_word)
#
# _dict = dict()
# for word in lst:
#     _dict[word] = _dict.get(word, 0) + 1
#
#
# _list = []
# for key, value in _dict.items():
#     _list.append((value, key))
#     _list.sort(reverse=True)
#
#
# print('First top 5 frequency words:')
# for freq, word in _list[0:5]:
#     print(f'{word:>5} -> {freq:>5}')






