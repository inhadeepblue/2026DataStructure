class Pokemon:
    # def __init__(self, hp, type, name):
    def __init__(self, hp, type, name=None):  # default parameter 값으로 None 할당
        self.name = name
        self.hp = hp
        self.type = type

pikachu = Pokemon(100, "Electric", "피카츄")
squirtle = Pokemon(200, "Water", "꼬부기")
charmander = Pokemon(150, "Fire")  # default parameter 안쓰면 error
print(charmander.name)  # default parameter로 할당된 None 출력
print(pikachu.type)
print(squirtle.hp)