def my_func(x, y):
    return x ** y

def my_func_1(x, y):
    z = x
    for i in range(1, -y):
        z = z * x
    result = 1 / z
    return result


x = float(input('Enter a positive float number: '))
y = int(input('Enter a negative integer number:  '))
print(f'The result using my_func is: {round(my_func(x, y), 2)}')
print(f'The result using my_func_1 is: {round(my_func_1(x, y), 2)}')
