from math import gcd
def ucln (x, y):
    a = gcd(x,y)
    return a
x = int(input("Nhap so X: "))
y = int(input("Nhap so Y: "))
ketqua = ucln(x,y)
print(ketqua)

