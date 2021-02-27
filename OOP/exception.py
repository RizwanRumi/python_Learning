result = None

a = float(input('Number 1: '))
b = float(input('Number 2: '))

try:
    result = a / b
except Exception as e:
    print("Error", e)
except ZeroDivisionError as e:
    print("ZeroDisionError: ", type(e))
except TypeError as e:
    print("TypeError: ", type(e))

print('Result = ', result)
print('End')