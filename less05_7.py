"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать.

"""
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
print(f'Average profit of profitable companies is: {round(profit_sum / profit_com_counter, 2)}$')
