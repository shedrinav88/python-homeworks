"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                    Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""
with open('Task_№6.txt') as f:
    subjects = f.readlines()
new_list = []
for string in subjects:
    new_list.append(string.split())
my_list = []
for i, value in enumerate(new_list):
    for el in value:
        if '(' in el:
            my_list.append((i, int(el[:el.index('(')])))
my_dict = {}
hours = 0
for el in new_list:
    for i in my_list:
        if i[0] == new_list.index(el):
            dict_key = el[0]
            hours += i[1]
            my_dict.update({dict_key: hours})
        else:
            hours = 0
            continue
print(f'Dictionary of subjects and learning hours: {my_dict}')




