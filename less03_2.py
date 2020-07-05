def user_description(name='user', surname='user', year_of_birth=1900,
                     city='city', email='user@usermail.com', phone=7900000000):
    return f'User description: {name} {surname}, was born in {year_of_birth}, ' \
           f'lives in {city}, e-mail: {email}, phone: {phone}'


user_1 = user_description('Ivan', 'Ivanov', 1986, 'Ekaterinburg', 'ivanov@yandex.ru', 79247384666)
print(user_1)
user_2 = user_description(year_of_birth=1969, name='Nikolay', surname='Petrov',
                          phone=79367563457, city='Tula', email='petrov@mail.ru')
print(user_2)
