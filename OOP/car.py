"""
class Car:
    pass

ford = Car()
honda = Car()
audi = Car()

# if pass is used in the class declaration, then attributes can create on the fly
ford.speed = 200
honda.speed = 220
audi.speed = 250

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

print(ford.speed)
print(ford.color)

ford.speed = 300
ford.color = 'green'

print(ford.speed)
print(ford.color)
"""

class Car:
    def __init__(self, speed, color):
        # private modifier by __
        self.__speed = speed
        self.__color = color

    # setter, getter method for speed and color
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(200, 'red')
honda = Car(220, 'red')
audi = Car(256, 'blue')

ford.set_speed(300)
ford.set_color('black')

print(ford.get_speed())
print(ford.get_color())

