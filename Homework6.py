#task1
word = str(input("Type word: "))
reverse_word = word[::-1]
if word == reverse_word:
     print('+')
else:
     print("-")

#task2
text = str(input("Type text: "))
find_word = str(input("Type word: "))
result = text.find(f'{find_word}')
if result != -1:
    print("yes")
else:
    print("No")

# task3
text = str(input("Type text: "))
check_init = text.startswith("abc")
if check_init:
    print("www" + text[3::])
else:
    print(text + "zzz")

# task4
text = str(input("Type text: "))
removed_numbers = ''
for i in text:
    if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        removed_numbers = removed_numbers + i
print(removed_numbers)

#task5
email = (input("Type text: "))
verify_for_dog = email.find("@")
verify_for_dot = email.find(".")
if verify_for_dot and verify_for_dog:
    print("yes")
else:
    print("no")
