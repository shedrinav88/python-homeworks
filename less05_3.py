"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
from functools import reduce

with open('Task_№3.txt') as f:
    my_list = f.readlines()
new_list = []
for i in range(len(my_list)):
    surname, salary = my_list[i].split()
    new_list.append((surname, salary))
for surname, salary in new_list:
    if float(salary) < 20000:
        print(f'Employee {surname} has a salary lower than 20 000 RUB ')
incomes = []
for salary in new_list:
    incomes.append(float(salary[1]))
cumul_income = reduce(lambda x, y: x + y, incomes)
print(f"Average employees's income is: {round(cumul_income/len(new_list), 2)}")
