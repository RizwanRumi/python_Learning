class eval_equations:

    # basic constructor
    def __init__(self, a):
        self.ans = a

        # expression 1

    @classmethod
    def eq1(cls, args):
        # create an object for the class to return
        x = cls((args[0] * args[0]) + (args[1] * args[1]) - args[2])
        return x

        # expression 2

    @classmethod
    def eq2(cls, args):
        y = cls((args[0] * args[0]) - (args[1] * args[1]))
        return y

        # expression 3

    @classmethod
    def eq3(cls, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = cls(temp)
        return z


li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0

# loop to get input three times
while i < 3:

    inp = li[i]

    # no.of.arguments = 2
    if len(inp) == 2:
        p = eval_equations.eq2(inp)
        print("equation 2 :", p.ans)

        # no.of.arguments = 3
    elif len(inp) == 3:
        p = eval_equations.eq1(inp)
        print("equation 1 :", p.ans)

        # More than three arguments
    else:
        p = eval_equations.eq3(inp)
        print("equation 3 :", p.ans)

        # increment loop
    i += 1