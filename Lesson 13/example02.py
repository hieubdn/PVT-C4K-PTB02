def gia_tri_tuyet_doi (n):
    if n < 0:
        return -n
    else:
        return n
so_nguyen = int(input("Nhap so nguyen: "))
ket_qua = gia_tri_tuyet_doi(so_nguyen)
print(ket_qua)
