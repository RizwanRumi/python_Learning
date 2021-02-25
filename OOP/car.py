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



