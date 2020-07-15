from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self, iterations):
        i = 0
        for light in cycle(self.__color):
            if i == int(iterations):
                break
            if light == 'red':
                print(light)
                sleep(7)
                i += 1
            elif light == 'yellow':
                print(light)
                sleep(2)
                i += 1
            elif light == 'green':
                print(light)
                sleep(3)
                i += 1


tf = TrafficLight()
tf.running(10)
