class Human:
    def __init__(self, gender, name="무명"):
        self.name = name
        self.gender = gender
        self.age = 1

    def eat(self, food):
        print(f"{self.name}이(가) {food}을(를) 먹습니다")


kyw = Human("여", "강예원")
ljm = Human("여")
print(kyw.name)
print(kyw.gender)
print(kyw.age)
print(ljm.name)
print(ljm.gender)
print(ljm.age)
ljm.name = "이정미"
print(ljm.name)
kyw.eat("햄버거")
