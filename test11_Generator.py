def my_iterable():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in my_iterable():
    print(i)

def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


even_num_list = list(even_numbers(10))
print(even_num_list)
