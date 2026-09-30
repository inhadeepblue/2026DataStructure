import array

a = array.array('f',(1.0, 1.5, 2.0, 2.5))
print(a)
print(a[1])
# a[1] = "1"  # TypeError: must be real number, not str
a[1] = -9.12
print(a)  # array('f', [1.0, -9.119999885559082, 2.0, 2.5]), IEEE754 부동소수점