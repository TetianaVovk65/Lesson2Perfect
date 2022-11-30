#task1
numbers = []
for i in range(5):
    number = input(f'Enter number {i} =')
    numbers.append(number)
print(numbers)


#task2
A = [1, 2, 3, 4, 5]
B = A.pop()
print(B)  # what was deleted
print(A)  # what we get after it

#task3
A = []
for i in range(10):
    number = int(input(f'Enter number {i} ='))
    A.append(number)
print(A)
find_number = int(input('Write number:'))
the_count = A.count(find_number)
print(f' The count is {the_count}')

#task4
ask_number = int(input('Write number:'))
A = []
for i in range(ask_number):
    number = int(input(f'Enter number {i} ='))
    A.append(number)
A.reverse()
print(f'reverse is {A}')

#task5
A = []
for i in range(5):
    number = int(input(f'Enter number {i} ='))
    A.append(number)
print(A)
C: list[int] = []
for c in A:
        if c > 5:
         C.append(c)
print(C)

#task6
ask_number = int(input('Write number:'))
A = []
for i in range(ask_number):
    number = int(input(f'Enter number {i} ='))
    A.append(number)
print(A)
max_ = A[0]
for ele in A:
        if ele > max_:
           max_ = ele

result_max = max_
print(f'Maximum = {result_max}')

min_ = A[0]
for ele in A:
    if ele < min_:
        min_ = ele
result_min = min_
print(f'Minimum = {result_min}')


#task7
text = str(input("Type text: "))
digit_counter = 0
for i in text:
    if i.isdigit():
        digit_counter += 1
if digit_counter != 0:
    print(digit_counter)
else:
    print("No numbers in the text")



