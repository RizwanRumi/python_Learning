result = None

a = float(input('Number 1: '))
b = float(input('Number 2: '))

try:
    result = a / b
except ZeroDivisionError as e:
    print("ZeroDisionError: ", type(e))
except TypeError as e:
    print("TypeError: ", type(e))
else:
    print('__else__')
finally:
    print('__Finally__')

print('Result = ', result)
print('End')