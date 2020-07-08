initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [i for i in initial_list if initial_list.count(i) == 1]
print(f'Элементы исходного списка, не имеющие повторений: {my_list}')
