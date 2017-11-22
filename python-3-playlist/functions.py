def area(radius):
    return (3.142 * radius * radius)

def vol(area, length):
    print(area * length)

radius = int(input('enter a radius:'))
length = int(input('enter a length:'))

vol(area(radius),length)
