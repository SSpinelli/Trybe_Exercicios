from abc import ABC, abstractclassmethod


class GeometricFigures(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def area():
        raise NotImplementedError

    @abstractclassmethod
    def perimeter():
        raise NotImplementedError


class Square(GeometricFigures):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rectangle(GeometricFigures):
    def __init__(self, base, height):
        self.__height = height
        self.__base = base

    def area(self):
        return self.__base * self.__height

    def perimeter(self):
        return (self.__base + self.__height) * 2


class Circle(GeometricFigures):
    def __init__(self, radius):
        self.__radius = radius
        self.__PI = 3.14

    def area(self):
        return self.__PI * (self.__radius**2)

    def perimeter(self):
        return (2 * self.__PI) * self.__radius


a = Square(4)
b = Rectangle(10, 7)
c = Circle(10)

print(a.perimeter())
print(b.perimeter())
print(c.perimeter())
