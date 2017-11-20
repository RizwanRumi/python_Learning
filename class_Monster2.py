class Monster:
    identity = "negative character"
    
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a hero, Mu... hahaha!!!")


# Create some real monster
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)


#check whether those monsters
#got different existence in memory or not

print('I am a ' + str(fogthing.heads) +
      ' headed ' + fogthing.identity)
print('I also have ' + str(mournsnake.heads) +
      ' headed ' + mournsnake.identity)
print('I got ' + str(tangleface.heads) +
      ' headed ' + tangleface.identity)


