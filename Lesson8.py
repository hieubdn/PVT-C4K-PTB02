n = int(input("nhập số: "))
sum = 0
i = 1
while sum < n:
    print(i, end="")
    sum += i
    i +=1

password = "123456789"
newPass = input("Nhập mật khẩu của bạn: ")
while (newPass != password):
    print("Sai gòi")
    newPass = input("Nhập mật khẩu của bạn: ")
print("Đúng gòi")

shop = ["gạo","mắm","muối","nước tương","nước mắm", "bột ngọt", "sữa chua"]
for i in range(len(shop)):
    a = shop[i]
    i += i
    print(a)