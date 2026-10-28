def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    print(f"{n}! = {result}")

def gugudan(d):
    print(f"{d}단!")
    for i in range(1, 10):
        print(f"{d} * {i} = {d*i}")

while True:
    choice = input('1) 구구단 2) 팩토리얼 3) 종료 : ')
    if choice == '1':
        dan = int(input("단(2~9) 입력 : "))
        gugudan(dan)
    elif choice == '2':
        number = int(input("정수 입력 : "))
        factorial(number)
    else:  # 1, 2외의 메뉴
        print("프로그램 종료")
        break  # 가장 가까운 반복문 탈출