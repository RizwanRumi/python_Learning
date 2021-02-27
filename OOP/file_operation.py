fh = open('demo.txt', 'a')

try:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+100))
finally:
    fh.close()