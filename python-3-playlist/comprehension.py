prizes = [5,10,50,100,1000]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)


nums=[1,2,3,4,5,6,7,8,9,10]
dbl_nums=[]
dbl_nums = [num**2 for num in nums if(num**2 % 2 == 0)]
print(dbl_nums)
