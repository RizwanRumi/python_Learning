from itertools import count, accumulate, takewhile, product, permutations

for i in count(3):
    print(i)
    if i>= 11:
        break


my_num=[1,2,3,4,5,6]
accum_num = accumulate(my_num)
list_of_accum_num = list(accum_num)
print(list_of_accum_num)


my_nums = [1,2,3,4,5,6,7,8,9,10,11,12]
num_less_six = takewhile(lambda x:x <= 6, my_nums)
filtered_nums = list(num_less_six)
print(filtered_nums)


letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
