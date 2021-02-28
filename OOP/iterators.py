class ListIterator:

    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]


a = [1, 10, 29, 33, 58]
mylist = ListIterator(a)
it = iter(mylist)

for i in it:
    print(i)
