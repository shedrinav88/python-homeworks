my_list = [1, 'python_task', [1, 6, [4, True]], False, {'name': 'Igor', 'age': 36}, b'Some content']
for i in my_list:
    print(f'Type of list element №{my_list.index(i)} is', type(my_list[my_list.index(i)]))
