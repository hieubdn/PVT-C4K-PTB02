# Câu hỏi: Chương trình này để làm gì?
sum = 0
for i in range(10): 
	if i % 2 == 0:
		sum = sum + i
print(sum)
# Trả lời: Tính tổng các số chẳng từ 0 đến 9

# -----***-----
# Câu hỏi: Vòng lặp này chạy bao nhiêu lần?
n = 5
for i in range (n+1):
		print("Xin chào, tôi là MindX")
# Trả lời: in ra 5 lần
# **********************------***************************

# Xuất ra màng hình dãy số thứ tự 1 -> 9
for i in range (10):
    print(i)

# Nhập 2 số nguyên a và b. 
# Tính tổng các số lẻ trong phạm vi a và b.
# Sau đó in ra màn hình kết quả
# ********---**********
# Bước 1: Khai báo biến chứa giá trị a và b, và biến chưas tổng số lẻ
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
sum = 0
# Bước 2: Lặp qua các giá trị trong phạm vi a và b
for i in range(a, b+1):
# Bước 3: Nếu là số lẽ thì cộng lại
    if i % 2 != 0:
        sum = sum + i
# Bước 4: in ra màng hình kết quả
print(sum)

# Viết bảng cửu chương từ 2 đến 9
print("Bảng cửu chương")
# Bước 1: Tạo vòng từ 2->9
for i in range(2, 10):
# Bước 2: Tạo vòng lặp từ 1 -> 10
    for j in range(1, 11):
# Bước 3: lấy giá trị vòng lặp 1 nhân giá trị vòng lặp 2
        result = i * j
# Bước 4: In ra kết quả
        print(i, " * ", j, " = ", result)
    print() # chú thích: Thêm một dòng trống sau mỗi hàng