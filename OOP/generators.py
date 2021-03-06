'''
Generator is a simple way for creating iterators
'''
# difference b2n iterators and generators:
# need to implement of iterators, iter and next method have to implement
# and it is lengthy and sometime counters are intuitive
# In generators no need to implement iter and next method, automatically implemented
# yield gives to return the immediate value and save the status of function


def myFunc():
    #yield 'a'
    #yield 'b'
    #yield 'c'

    # n = 1
    # print('-----------', n)
    # yield n
    # n += 1
    # print('-----------', n)
    # yield n
    # n += 1
    # print('-----------', n)
    # yield n

    for i in range(3):
        print('-----------', i)
        yield i

x = myFunc() # returns iterator object

print(next(x))
print(next(x))
print(next(x))
#print(next(x))

print("same example to implement with generators which is implemented by iterators\n")

def list_iterator(list):
    for i in list:
        yield i

a = [1, 2, 3, 6, 5, 4]
mylist = list_iterator(a)

for i in mylist:
    print(i)