from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def __init__(self, name, size, height):
        pass


class AbstractCoat(AbstractClothes):
    @abstractmethod
    def coat_cloth(self):
        pass


class AbstractCostume(AbstractClothes):
    @abstractmethod
    def costume_cloth(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height


class Coat(AbstractCoat, Clothes):
    @property
    def coat_cloth(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(AbstractCostume, Clothes):
    @property
    def costume_cloth(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat('Coat', 42, 1.72)
coat_c = coat.coat_cloth
print(f'A coat needs {coat_c} meters of cloth')
costume = Costume('Costume', 42, 1.72)
costume_c = costume.costume_cloth
print(f'A costume need {costume_c} meters of cloth')
