# # K = []
# # t = ["a ", "b ", "c ", "d "]
# # for i in range (4):
# #     R = int(input(f"nhập số {t[i]}: "))
# #     K.append(R)
# # print(K)

# # lst = [7, 86, 32, 54, 90, 65, 39, 64]
# # sum = 0 
# # for i in lst: 
# #     if i % 2 != 0:
# #         sum += i
# # print(sum)

# new = []
# old = [ "a" , "b", "c", "d"]
# for i in range(4):
#     ipt = int(input(f"nhập số {old[i]}: "))
#     new.append(ipt)
# print(new)

# *****Bài kiểm tra****
# Câu 1
A = [5, 12, 15, 7, 7, 30, 3, 56]
tong_chan = 0

for phan_tu in A:
    if phan_tu % 2 == 0:  # Kiểm tra xem phần tử có phải là số chẵn hay không
        tong_chan += phan_tu

print(f"Tổng các số chẵn trong danh sách A là: {tong_chan}")

# Câu 2
# Khởi tạo danh sách để lưu số tiền chi tiêu hàng ngày
chi_tieu_ngay = []
ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

# Nhập số tiền chi tiêu hàng ngày
for i in range(7):
    chi_tieu = float(input(f"Nhập số tiền chi tiêu cho {ngay_trong_tuan[i]}: "))
    chi_tieu_ngay.append(chi_tieu)

# Tính tổng chi tiêu trong tuần
tong_chi_tieu = sum(chi_tieu_ngay)

# Tìm ngày chi tiền nhiều nhất trong tuần
ngay_nhieu_tien_nhat = ngay_trong_tuan[chi_tieu_ngay.index(max(chi_tieu_ngay))]

# Tính trung bình chi tiêu hàng ngày
trung_binh_chi_tieu = tong_chi_tieu / 7

# Hiển thị các thông tin thống kê
print(f"Tổng chi tiêu trong tuần: {tong_chi_tieu} VNĐ")
print(f"Ngày chi tiền nhiều nhất trong tuần: {ngay_nhieu_tien_nhat}")
print(f"Trung bình chi tiêu hàng ngày trong tuần: {trung_binh_chi_tieu} VNĐ")
# Chương trình này cho phép bạn nhập số tiền chi tiêu hàng ngày trong tuần, tính tổng chi tiêu trong tuần, tìm ngày chi tiền nhiều nhất, và tính trung bình chi tiêu hàng ngày trong tuần.




