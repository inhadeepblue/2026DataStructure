class Human:
    def __init__(self, gender, name="무명"):
        self.name = name
        self.gender = gender
        self.age = 1

    def eat(self, food):
        print(f"{self.name}이(가) {food}을(를) 먹습니다")

    def __str__(self):
        return f"{self.name}은(는) {self.age}살이고 {self.gender}성 입니다."


kyw = Human("여", "강예원")
ljm = Human("여")
print(kyw)
print(ljm)
ljm.name = "이정미"
print(ljm.name)
kyw.eat("햄버거")
print(ljm)
