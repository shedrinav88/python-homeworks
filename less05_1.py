"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('my_first.txt', 'w') as f:
    while True:
        my_str = input('Enter a string: ')
        if my_str == '':
            break
        else:
            f.writelines(my_str + '\n')
            continue
print('File was successfully created!')
