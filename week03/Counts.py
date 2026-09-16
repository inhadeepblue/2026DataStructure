n = int(input("정수 입력 : "))
count = 0
for i in range(1, n+1):
    print(i)
    count += i  # count = count + i
    # print(count)
print(f"1부터 {n}까지 누산 합계는 {count}입니다.")