class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self):
        r_square = self._length * self._width
        weight_5sm= 25 * 5
        rw = r_square * weight_5sm
        return rw


r = Road(20, 5000)
print(f'Asphalt weight for a road with entered parameters is {r.road_weight()/1000} tons')


