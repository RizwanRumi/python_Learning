class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            #print('Coffee Too Hot ')
            #raise Exception('Coffee Too Hot ')
            raise CoffeeTooHotException('Coffee temperature: ' + str(self.__temperature))
        elif self.__temperature < 65:
            # print('Coffee Too Cold ')
            raise CoffeeTooColdException('Coffee temperature: ' + str(self.__temperature))
        else:
            print('Coffee OK to Drink ')

cup = CoffeCup(10)
cup.drink_coffee()