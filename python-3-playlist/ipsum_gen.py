from random import randint

ninja_words=[
    'Aiki', 'Buyu','Chimonojustsu','Cho sen','Dojo','Gakusei',
    'haiboku','Jin','Kenshi','Obake ken','Rakusha','Sammaru','Tekkon','Yoko'
]

def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f'{word} {ninja_words[random_pos]}'

paragraphs = int(input('how many paragraphs of you want? : '))

with open('ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paragraphs):
        ninja_text = list(map(ninjarize, items))
        with open('ninja_ipsum.txt','a') as ipsum_ninja:
            ipsum_ninja.write(''.join(ninja_text) + '\n\n')
