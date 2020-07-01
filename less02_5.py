my_list = [7, 5, 3, 3, 2]
print(f'Initial rating list is: {my_list}')
user_number = int(input('Enter an integer: '))
for number in my_list:
    if user_number > number:
        my_list.insert(my_list.index(number), user_number)
        break
    elif my_list.index(number) == len(my_list) - 1:
        my_list.append(user_number)
        break
print(f'Rating list now is: {my_list}')
