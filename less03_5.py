def my_func(my_list):
    """
    Функция принимает строку чисел, разделенных пробелом и
    выводит сумму введенных чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
    и сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Если пользователь введет в строке символ "q", то при нажатии на Enter
    выполнение программы завершается. Все прочие символы игнорирутся программой и
    складываются только введенные числа.
    Если символ "q" введен после нескольких чисел, то вначале сумму этих чисел
    добавляется к полученной ранее сумме и после этого программа завершается.
    """
    result = 0
    while True:
        my_new_list = my_list.split()
        if 'q' in my_new_list:
            list_of_numbers = []
            for i in my_new_list:
                try:
                    i = int(i)
                    list_of_numbers.append(i)
                except ValueError:
                    result += sum(list_of_numbers[:my_new_list.index('q')])
            break
        else:
            list_of_numbers = []
            for i in my_new_list:
                try:
                    i = int(i)
                    list_of_numbers.append(i)
                except ValueError:
                    continue
            result += sum(list_of_numbers)
            print(f'Sum of all entered numbers is {result}')
            my_list = input('Enter the row of numbers splitted by the space: ')
    return result


my_list = input('Enter the row of numbers splitted by the space: ')
print(f'Final sum of all entered numbers till "q" symbol is {my_func(my_list)}')



