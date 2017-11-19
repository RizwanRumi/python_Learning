

# map using
def make_twice(x):
    return x * 2

my_list=[10,20,30]
result = map(make_twice, my_list)
print(list(result))


#filter using
def is_even(x):
    return x % 2 == 0

my_numbers = [1,2,3,4,5,6]
result = filter(is_even, my_numbers)
print(list(result))

#using lambda

numbers = [5,10,15]
result = map(lambda x: x*2,numbers)
print(list(result))



numbers = [1,2,3,4,5,6,7,8,9,10,11]
result = filter(lambda x: x%2==0,numbers)
print(list(result))
