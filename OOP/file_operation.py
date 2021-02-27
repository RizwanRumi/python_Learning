'''
fh = open('demo.txt', 'a')

try:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+100))
finally:
    fh.close()
'''

# use 'with' keyword instead of explicit of previous code which has used try and finally

with open('demo.txt', 'a') as fh:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+200))