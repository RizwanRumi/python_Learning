with open('files/write.txt','w') as write_file:
    write_file.write('Hey there ninjas, python is awesome')

# junk

with open('files/write.txt','a') as write_file:
    write_file.write('\nI love it so much, I dream in python')

quotes = [
 '\nI can resist everything except temptation',
 '\nWe are all in gutter, but some of us are looking at the stars',
 '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt','a') as write_file:
    write_file.writelines(quotes)
