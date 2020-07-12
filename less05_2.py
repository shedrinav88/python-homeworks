"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('Task_№2.txt') as f:
    my_list = f.readlines()
print(f'File Task№2.txt consists of {len(my_list)} string(s):')
for i, string in enumerate(my_list, 1):
    print(f'String №{i} consists of {len(string.split())} word(s)')
