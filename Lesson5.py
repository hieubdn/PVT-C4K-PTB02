# *****Xếp Hạng học sinh*****
# diem = float(input("Nhập số điểm của học sinh: "))
# if diem >= 8:
#     print("Học sinh đạt học sinh Giỏi")
# elif diem >=6.5:
#     print("Học sinh đạt học sinh Khá")
# elif diem >= 5:
#     print("Học sinh đạt học sinh Trung Bình")
# else: 
#     print("Học sinh Yếu")

# *****Bài Kiểm Tra*****
# ****Câu 1****
loaiGiay = int(input("Nhập ký hiệu loại giấy: "))
soTrang = int(input("Số trang giấy cần in: "))
if loaiGiay == 1 and soTrang % 2 == 1:
    luong_giay_can_dung = int((soTrang / 2) + 1) 
    print("Lượng giấy cần dùng để in được tài liệu 2 mặt là: ", luong_giay_can_dung)
else: 
    if loaiGiay == 2:
        print("Lượng giấy cần dùng để in quảng cáo 1 mặt là: ", soTrang)
# ****Câu 2****
print("*** Tính số tiền điện tiêu thụ trong tháng ***")
kwh = int(input("Nhập vào số KWH điện tiêu thụ trong tháng: "))
if kwh <= 50:
    total_amount = kwh * 1700
elif 51 <= kwh <= 100:
    total_amount = 50 * 1700 + (kwh - 50) * 1900
elif 101 <= kwh <= 200:
    total_amount = 50 * 1700 + 50 * 1900 + (kwh - 100) * 2100
else: 
    total_amount = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kwh - 200) * 3000
print("Số tiền điện cần phải trả: ", total_amount, "Đồng")