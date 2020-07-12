from functools import reduce

even_num = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(lambda x, y: x * y, even_num)
print(f'Произведение всех четных чисел от 100 до 1000 (включительно): {result}')
