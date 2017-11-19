file_to_work = open("Test.txt", "r")

"""
content = file_to_work.read()

print(content)


print('\n')
"""

"""
just_one_char = file_to_work.read(1)
print(just_one_char)

remain_four_char = file_to_work.read(4)
print(remain_four_char)

rest_part = file_to_work.read()
print(rest_part)

"""

# lines = file_to_work.readlines()
# print(lines)

for my_line in file_to_work:
    print(my_line)

file_to_work.close()


