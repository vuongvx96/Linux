

from SV_Khoa import *

KHOA = []
KHOA.append(Khoa("01","CNTT"))
KHOA.append(Khoa("02","Ke Toan"))
KHOA.append(Khoa("03","Co Khi"))
KHOA.append(Khoa("04","Nuoi Trong TS"))

DSSV = []
DSSV.append(SinhVien("001","Mai A","01"))
DSSV.append(SinhVien("002","Tran B","01"))
DSSV.append(SinhVien("003","Van C","02"))
DSSV.append(SinhVien("004","Thi K","01"))

# Xuat danh sach sinh vien
print"\nDanh sach sinh vien:"
for sv in DSSV:
	sv.XuatTT()

# Xuat danh sach khoa
print "\nDanh sach khoa"
for k in KHOA:
	k.Xuat()

print "\nDanh sach sinh vien khoa CNTT"
# Tim ma khoa CNTT
ma = ""
for k in KHOA:
	if (k.TenKhoa == "CNTT"):
		ma = k.getMaKhoa()
		break;

for sv in DSSV:
	if (sv.getMaKhoa() == ma):
		sv.XuatTT()

