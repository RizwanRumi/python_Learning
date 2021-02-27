fh = open('demo.txt', 'w')

try:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+1))
finally:
    fh.close()