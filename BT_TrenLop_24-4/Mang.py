# Mang trong Python
#-- Ham nhap mang
def Nhapmang(arr,n):
	for i in range(n):
		arr.append(int(raw_input("Nhap vao phan tu thu %d = " %(i+1))))

#-- In mang vua nhap
def Xuatmang(arr):
	for item in arr:
		print item,

#-- Ham xuat cac phan tu chan
def Inchan(arr):
	for item in arr:
		if (int(item) % 2 == 0):
			print item,

#-- Ham sap xep mang tang dan
def Sapxep(arr,n):
	for i in range(0,n-1):
		for j in range(i+1,n):
			if (a[i] > a[j]):
				tam = a[i]
				a[i] = a[j]
				a[j] = tam

#-- Ghi ra file
def Ghifile(arr):
	file = open('Mang.txt','w+')
	for item in arr:
		file.write(str(item) + " ")
	file.close()


#----------- CHUONG TRINH CHINH -------------
# Khai bao mang a
a = []
n = input("Nhap vao so luong phan tu: ")
Nhapmang(a,n)
print("\nMang vua nhap:")
Xuatmang(a)
print("\nCac phan tu co gia tri chan:")
Inchan(a)
print("\nMang sau khi sap xep tang dan:")
Sapxep(a,n)
Xuatmang(a)
print("\nGhi ra file ...")
Ghifile(a)





