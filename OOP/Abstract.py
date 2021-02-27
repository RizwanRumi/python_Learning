'''
cannot create instance of abstract class
subclass must be implemented of super class methods
use ABC module (Abstract based class) in Abstract class
use decorator to declare abstract method
'''

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
        