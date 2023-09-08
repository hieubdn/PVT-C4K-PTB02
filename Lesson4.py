# Thầy giáo mang kẹo làm quà cho cả lớp nhân dịp lớp có kết quả kiểm tra tốt.
# Túi kẹo có n viên và lớp có m học sinh. Số kẹo được chia đều cho tất cả học sinh trong lớp. 
# Viết chương trình: Nhập n và m vào từ bàn phím.
# đưa ra màn hình số kẹo mỗi học sinh nhận được và số kẹo còn thừa sau khi chia.
n = int(input("Nhập số kẹo hiện tại đang có: "))
m = int(input("Nhập số học viên: "))
a = n//m
b = n%m
print("số kẹo học viên có thể nhận được là: ", a)
print("số kẹo còn thừa lại là: ", b)


# Nhập một số giây từ bàn phím - Viết chương trình chuyển đổi số giây qua Giờ - Phút - giây
s = int(input("Số giây: "))
gio = s // 3600
phut = (s % 3600) // 60
giay = s % 60
print("Chuyển đổi: ", gio, "giờ", phut, "phút", giay, "giây")


# Nhập một số từ bàn phím và tính giá trị tuyệt đối của số đó
n = int(input("Nhập một số: "))
if n < 0:
    b = n * (-1)
    print(b,"là giá trị tuyệt đối của", n)
else:
    print(n, "là giá trị tuyệt đối của", n)
