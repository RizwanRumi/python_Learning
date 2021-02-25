# from file name import class name
from rectangle import Rectangle
from triangle import Triangle


rect = Rectangle()
tri = Triangle()

rect.set_values(50, 40)
tri.set_values(50, 40)

print(rect.area())
print(tri.area())