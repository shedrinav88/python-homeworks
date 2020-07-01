i = 1
add_good = input('Do you want to enter a new good? (Y/N) ')
goods_list = []
while add_good == 'Y':
    name = input('Enter the name of the good: ')
    price = float(input('Enter the price of the good: '))
    quantity = float(input('Enter the quantity of goods: '))
    measure = input('Enter the measure unit: ')
    good = (i, {'name': name, 'price': price, 'quantity': quantity, 'measure unit': measure })
    goods_list.append(good)
    i += 1
    add_good = input('Do you want to enter a new good? (Y/N): ')
print('List of the goods is the following: ')
for elem in goods_list:
    print(elem)
