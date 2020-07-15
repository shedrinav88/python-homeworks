class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car starts to go!')

    def stop(self):
        print('The car stops!')

    def turn(self, direction):
        print(f'The car turns {direction}')

    def show_speed(self, cur_speed):
        print(f'Current speed is {cur_speed}km/h')


class TownCar(Car):
    def show_speed(self, cur_speed):
        print(f'{self.name} is over speeding!') if cur_speed > 60 else print(f'Current speed is {cur_speed}km/h')


class WorkCar(Car):
    def show_speed(self, cur_speed):
        print(f'{self.name} is over speeding!') if cur_speed > 40 else print(f'Current speed is {cur_speed}km/h')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


tc = TownCar(250, 'grey', 'Mercedes')
print(f'This car is a {tc.color} {tc.name}, which max speed is {tc.speed}km/h')
tc.stop()
tc.go()
tc.turn('left')
tc.show_speed(80)
tc.show_speed(50)
print(tc.is_police)

pc = PoliceCar(180, 'white-blue', 'Ford')
print(pc.is_police)
pc.show_speed(40)
