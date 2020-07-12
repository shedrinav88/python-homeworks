"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('numbers.txt', 'w') as f:
    f.write(input('Enter a row of numbers divided by a space: '))
with open('numbers.txt') as new_f:
    numbers = new_f.readline()
    numbers = map(float, numbers.split())
numbers_sum = sum(numbers)
print(f'The sum of numbers in numbers.txt file is: {numbers_sum}')
