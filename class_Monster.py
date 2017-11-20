class Monster:
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

print('I have ' + str(fogthing.heads) +
      ' heads and I\'m ' + fogthing.color)
print('I also have ' + str(mournsnake.heads) +
      ' heads and I\'m ' + mournsnake.color)
print('I got ' + str(tangleface.heads) +
      ' heads and I\'m ' + tangleface.color)

mournsnake.attack()
