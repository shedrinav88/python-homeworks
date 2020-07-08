from itertools import count, cycle

# итератор, генерирующий целые числа, начиная с указанного
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

print('Next script --------------------')
# итератор, повторяющий элементы некоторого списка, определенного заранее.
my_list = [5, 4, 3, 2, 1, 'start']
c = 0
for el in cycle(my_list):
    if c > 11:
        break
    print(el)
    c += 1
