x = 1
n = int(input("Input factorial number : "))
for i in range(1,n+1):
    x = x * i
print(f"{n}! = {x}")
# O(n) Time complexity
# O(1) Space complexity