from math import factorial


def fact(n):
    for el in range(1, n+1):
        yield factorial(el)


n = int(input('Enter the value of "n": '))
for el in enumerate(fact(n), 1):
    print(f'Factorial of {el[0]} is {el[1]}')
