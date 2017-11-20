class A:
    def where(self):
        print("I am from class A")


class B:
    def where(self):
        print("I am from class B")


class C(A, B):
    pass


an_instance_of_c = C()
an_instance_of_c.where()

# C -> A -> B
print(C.mro())

print('\n using super method:')

#using super method inherited method from base class

class X:
    def spam(self):
        print(1)

class Y(X):
    def spam(self):
        print(2)
        super().spam()


Y().spam()
