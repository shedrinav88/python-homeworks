start_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_numbers = [start_numbers[el+1] for el in range(len(start_numbers)) if el != len(start_numbers) - 1
              and start_numbers[el+1] > start_numbers[el]]
print(f'List of elements that are larger than their previous elements: {my_numbers}')
