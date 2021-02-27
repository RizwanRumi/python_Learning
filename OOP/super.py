class Parent:
    def __init__(self, name):
        print('Parent__init__', name)

class Parent2:
    def __init__(self, name):
        print('Parent2__init__', name)

class Child(Parent2, Parent):
    def __init__(self):
        print('Child__init__')
        # if you want to call both parent class __init__ function
        # super().__init__('max')
        Parent.__init__(self, 'max')
        Parent2.__init__(self, 'tom')

child = Child()
# method resolution order (__mro)
print(Child.__mro__)