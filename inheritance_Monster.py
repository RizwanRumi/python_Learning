class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking....')


class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrr\n')


class Mournsnake(Monster):
    def make_sound(self):
        print('Hiiisssshhh\n')



fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()



mournsnake = Mournsnake("Mournsnake", "Yellow")
mournsnake.attack()
mournsnake.make_sound()
