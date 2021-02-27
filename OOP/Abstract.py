'''
Cannot create instance of abstract class.
Subclass must be implemented of abstract methods from base class
use @abstractmethod decorator to declare an abstract method
'''
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


# shape = Shape() # can't instantiate because of abstract class
square = Square(5)
print(square.area())
print(square.perimeter())
