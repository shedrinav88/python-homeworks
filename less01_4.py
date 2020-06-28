"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = input('Enter some positive integer number: ')
i = 0
max_digit = 0
while i < len(number):
    if int(number[i]) >= max_digit:
        max_digit = int(number[i])
    i += 1
print(f'maximum digit in your number is {max_digit}')

# можно проще, но мы этого еще не изучали
number = input('Enter some positive integer number: ')
numbers_list = [int(i) for i in number]
print(f'maximum digit in your number is {max(numbers_list)}')
