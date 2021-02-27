'''
Multiple constructors are required when the class has to perform
different actions on different parameters.

python does not support explicit multiple constructors, yet there
are some ways using which the multiple constructors can be achieved

1) Overloading constructors based on arguments (*args -> tuple,
**args -> dictionary)
2) Calling methods from __init__
3) Using @Classmethod decorator
'''