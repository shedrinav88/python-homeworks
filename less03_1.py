def my_div(divd,  divr):
    try:
        result = divd / divr
        return result
    except ZeroDivisionError:
        print("Divider can't be a zero")


dividend = float(input('Enter the dividend: '))
divider = float(input('Enter the divider: '))
div_2_numbers = my_div(dividend, divider)
print(f'The result of division is: {div_2_numbers}')
