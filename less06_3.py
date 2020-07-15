class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return income


obj = Position('Fedor', 'Petrov', 'Manager', 100000, 25000)
print(f'Full name is: {obj.get_full_name()}')
print(f'Total income is: {obj.get_total_income()} RUB')
print(f'Position is: {obj.position}')
