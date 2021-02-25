# from file name import class name
from polygon import Polygon
# multiple inheritance
from shape import Shape


class Triangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height() / 2