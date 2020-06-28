"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

seconds = int(input('Введите время в секундах: '))
hours = str(seconds // 3600)
minutes = str((seconds % 3600) // 60)
seconds_left = str((seconds % 3600) % 60)
if len(hours) < 2:
    hours = '0' + hours
if len(minutes) < 2:
    minutes = '0' + minutes
if len(seconds_left) < 2:
    seconds_left = '0' + seconds_left
print(f'The result in format hh:mm:ss is {hours}:{minutes}:{seconds_left}')
