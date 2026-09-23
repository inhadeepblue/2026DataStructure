x = 1
n = int(input("Input factorial number : "))
a_list = list()
for i in range(1,n+1):
    a_list.append(x)
    x = x * i
print(f"{n}! = {x}")
print(a_list)
# O(n) Space complexity