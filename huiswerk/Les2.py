class Character:
    speed = 40
    alive = True
    sprite = None
    points = 0

    def __init__(self):
        print("Dit is de constructor van Char")

    def Walk(self):
        print("Char loopt met snelheid", self.speed)
    

class Inheritance(Character):

    lives = 3
    item = None

    def __init__(self):
        super().__init__()
        self.speed = 30

    def Walk(self):
        print("Inheritance is snel, namelijk:", self.speed)

    def Jump(self):
        print("Inheritance kan blijkbaar springen!")


characterA = Character()
InheritanceX = Inheritance()

characterA.Walk
InheritanceX.Walk
InheritanceX.Jump

print(characterA.speed)
print(InheritanceX.speed)
print(InheritanceX.lives)