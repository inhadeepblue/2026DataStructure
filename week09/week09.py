def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    print(f"{n}! = {result}")

def gugudan(d):
    print(f"{d}단!")
    for i in range(1, 10):
        print(f"{d} * {i} = {d*i}")

print('구구단 & 팩토리얼')
number = int(input("정수 입력 : "))
gugudan(number)
factorial(number)