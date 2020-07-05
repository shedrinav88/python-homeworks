# решение через list
seasons = ['winter', 'spring', 'summer', 'autumn']
try:
    user_month = int(input('Enter the month as a number from 1 to 12: '))
    if user_month == 1 or user_month == 2 or user_month == 12:
        print(f'Your month is in {seasons[0]}')
    elif user_month == 3 or user_month == 4 or user_month == 5:
        print(f'Your month is in {seasons[1]}')
    elif user_month == 6 or user_month == 7 or user_month == 8:
        print(f'Your month is in {seasons[2]}')
    elif user_month == 9 or user_month == 10 or user_month == 11:
        print(f'Your month is in {seasons[3]}')
    else:
        print('No such month and season')
except ValueError:
    print('You need to enter an integer from 1 to 12!')

# решение через dict
seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
           9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
try:
    user_month = int(input('Enter the month as a number from 1 to 12: '))
    try:
        if seasons[user_month]:
            print(f'Your month is in {seasons[user_month]}')
    except KeyError:
        print('No such month and season')
except ValueError:
    print('You need to enter an integer from 1 to 12!')

