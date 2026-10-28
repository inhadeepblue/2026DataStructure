def gugudan(d):
    print(f"{d}단!")
    for i in range(1, 10):
        print(f"{d} * {i} = {d*i}")

print('구구단 & 함수')
dan = int(input("정수 입력(단 입력) : "))
gugudan(dan)