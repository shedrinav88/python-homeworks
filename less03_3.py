def my_func(x1, x2, x3):
    my_list = [x1, x2, x3]
    my_list = sorted(my_list)
    return sum(my_list[1:])


x1 = float(input('Enter the first argument: '))
x2 = float(input('Enter the second argument: '))
x3 = float(input('Enter the third argument: '))
print(f'The arguments are {x1}, {x2}, {x3}')
sum_2_max = my_func(x1, x2, x3)
print(f'The sum of 2 max arguments: {sum_2_max}')
