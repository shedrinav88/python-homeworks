"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
numbers_dict = {'One': 'Один','Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Task_№4.txt') as f:
    my_list = f.readlines()
new_list = []
for string in my_list:
    new_list.append(string.split(' — '))
with open('russian_vers.txt', 'w', encoding='utf-8') as new_f:
    for el in new_list:
        new_f.writelines(f'{numbers_dict[str(el[0])]} - {el[1]}')
print('New file was successfully created!')
