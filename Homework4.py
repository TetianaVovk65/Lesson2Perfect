# task1
number1 = int(input('a='))
number2 = int(input('b='))
number3 = int(input('c='))

if (number1 > 10) and (number2 > 10) and (number3 > 10) and (number1 / 3) and (number2 / 3):
    print('yes')
else:
    print('no')

# task2
number1 = int(input('a='))
number2 = int(input('b='))
number3 = int(input('c='))

if (number1 > number2) and (number1 > number3):
    print(f'max is {number1}')
elif (number2 > number1) and (number2 > number3):
    print(f'max is {number2}')
else:
    print(f'max is {number3}')

# task with *
number = int(input("Enter 3 significant number:  "))

a = number // 100
b = (number // 10) % 10
c = number % 10

reversed_number = (str(c) + str(b) + str(a))
print(reversed_number)
