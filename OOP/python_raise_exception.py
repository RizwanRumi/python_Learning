class CoffeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            #print('Coffee Too Hot ')
            raise Exception('Coffee Too Hot ')
        elif self.__temperature < 65:
            # print('Coffee Too Cold ')
            raise Exception('Coffee Too Cold ')
        else:
            print('Coffee OK to Drink ')

cup = CoffeCup(10)
cup.drink_coffee()