number_of_elem = int(input("Enter the number of list's elements: "))
i = 0
my_list = []
while i < number_of_elem:
    my_element = input(f'Enter your element № {i + 1} (it will be str class): ')
    my_list.append(my_element)
    i += 1
print(f'Initial view of the list {my_list}')
for elem in range(len(my_list)):
    if elem == 0 or elem % 2 == 0:
        try:
            my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
        except IndexError:
            break
print(f'View of the list after reversing neighbor elements: {my_list}')
