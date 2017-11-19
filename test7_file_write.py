file_to_work = open("Test.txt", "w")

is_writing_done = file_to_work.write("I am writing!!!")

if is_writing_done:
    print("Yes, {0} byte(s) has been written".format(is_writing_done))

file_to_work.close()

# best way to read and write using with

with open("Test.txt") as f:
    print(f.read())
