a = "MindX Technology Shoool"
b = "MindX"
c = "School"
f = b in a
e = c in a
g = a.find(b)
h = a.find(c)
k = a.replace("Shoool", "School")
print(f)
print(e)
print(g)
print(h)
print(k)

# Bài 1:
ho_ten = input("Nhập họ và tên: ")
vi_tri_khoang_trang_dau_tien=ho_ten.find(' ')
ho = ''
for i in range(vi_tri_khoang_trang_dau_tien):
    ho += ho_ten[i] 
print("Họ của người bạn là:", ho)

# Bài 2:
s = input("Nhập vào ngày tháng năm (dd/mm/yyyy): ")
result = "Ngày "  + s # Ngày dd/mm/yyyy
result = result.replace('/', ' tháng ', 1) # Ngày dd tháng mm/yyyy
result = result.replace('/', ' năm ') # Ngày dd tháng mm năm yyyy
print(result)