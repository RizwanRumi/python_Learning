
"""
default arguments example for *args, **kwargs in python
"""

print("args for single value: \n")

def student1(name, age, marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)

student1('Tom', 22, 85)


print("\n*args for multiple values und result shows by tuple: \n")

def student2(name, age, *marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)

student2('Jerry', 22, 95, 63, 87)


print("\n**args for multiple values und result shows by dictionary : \n")

def student3(name, age, **marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)
    for key, value in marks.items():
        print(key, ' ', value)

student3('Jerry', 22, english=95, math =63, physics=87)

