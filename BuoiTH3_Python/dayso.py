# Day so
def NhapMang(arr, n):
	for i in range(n):
		arr.append(raw_input("Nhap vao so thu %d = " %(i+1)))


def XuatMang(arr):
	print "\nDay so vua nhap: "
	for item in arr:
		print item,

def Tong_So_Chan(arr):
	sum = 0.0
	for item in arr:
		if (int(item) % 2 == 0):
			sum = sum + int(item)
	return sum

a = []
n = input("\nNhap vao so luong phan tu: ")

# Cau a) In ra man hinh day so vua nhap
NhapMang(a,n)
XuatMang(a)

# Cau b) Tinh tong cac phan tu chan cua day
print "Tong cac so chan co trong day:", Tong_So_Chan(a)

