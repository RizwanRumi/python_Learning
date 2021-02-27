# If multiple __init__ methods are written for the same class,
# then the latest one overwrites all the previous constructors.

class example:

    def __init__(self):
        print("One")

    def __init__(self):
        print("Two")

    def __init__(self):
        print("Three")

e = example()

print('''
Solution: Constructors overloading
based on arguments (*args -> tuple, **args -> dictionary)
''')

class sample:

    def __init__(self, *args):

        # if args are more than 1
        # sum of args
        if len(args) > 1:
            self.ans = 0
            for i in args:
                self.ans += i

                # if arg is an integer
        # square the arg
        elif isinstance(args[0], int):
            self.ans = args[0] * args[0]

            # if arg is string
        # Print with hello
        elif isinstance(args[0], str):
            self.ans = "Hello! " + args[0] + "."


s1 = sample(1, 2, 3, 4, 5)
print("Sum of list :", s1.ans)

s2 = sample(5)
print("Square of int :", s2.ans)

s3 = sample("Constructors")
print("String :", s3.ans)