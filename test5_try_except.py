try:
    a = 100
    b = int(input("Enter a divisor to divide 100: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")


print("\n")

try:
    variable = 10
    # print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divide by zero")
except (ValueError, TypeError):
    print("Type or value error occurred")

print("\n")

try:
    word = "spam"
    print(word/0)
except:
    print("An error occurred")

print('\n')

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("This code will run no matter what")

print('\n')

try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")

print('\n')

try:
    num = 5 / 0
except:
    print("custom message about an error!")
    raise
    
