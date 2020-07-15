"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('Task_№7.txt') as f:
    my_list = f.readlines()
data_set = []
for el in my_list:
    data_set.append(el.split())
for i, value in enumerate(data_set):
    profit = float(value[2]) - float(value[3])
    print(f'Financial result of {data_set[i][1]} {data_set[i][0]} is: {profit}$')
    data_set[i].append(profit)
profit_sum = 0
profit_com_counter = 0
for i in range(len(data_set)):
    if data_set[i][4] > 0:
        profit_sum += data_set[i][4]
        profit_com_counter += 1
av_profit = round(profit_sum / profit_com_counter, 2)
print(f'Average profit of profitable companies is: {av_profit}$')
final_dict = {}
for i in range(len(data_set)):
    final_dict.update({data_set[i][0]: data_set[i][4]})
av_profit_dict = {'average_profit': av_profit}
result_list = [final_dict, av_profit_dict]
with open('result_dict.json', 'w') as new_f:
    json.dump(result_list, new_f)
print(f'result_dict.json was successfully created')
