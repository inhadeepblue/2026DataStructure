class Pokemon:
    def __init__(self, name, hp, type):
        self.name = name
        self.hp = hp
        self.type = type

pikachu = Pokemon("Pikachu", 100, "Electric")
squirtle = Pokemon("Squirtle", 200, "Water")
print(pikachu.type)
print(squirtle.hp)