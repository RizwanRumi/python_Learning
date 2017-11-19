def my_decorator(func):
    def decorate():
        print('-----------')
        func()
        print('-----------')
    return decorate


@my_decorator # if we add this 
def print_raw():
    print('Clear Text')


print_raw()

# result = my_decorator(print_raw)
# result()
