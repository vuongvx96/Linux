class HCN:
	dai = 0,
	rong = 0,
	ten = ""
	#Cac phuong thuc
	#-- Phuong thuc khoi tao
	def __init__(self,dai,rong,ten):
		self.dai = dai
		self.rong = rong
		self.ten = ten

	def getChieuDai(self):
		return self.dai
	def setChieuDai(self,dai):
		self.dai = dai

	def getChieuRong(self):
		return self.rong
	def setChieuRong(self,rong):
		self.rong = rong

	def getTen(self):
		return self.ten
	def setTen(self,ten):
		self.ten = ten

	# 1. Phuong thuc tinh chu vi
	def getChuVi(self):
		return (self.dai+self.rong)*2
	# 2. Phuong thuc tinh dien tich
	def getDienTich(self):
		return (self.dai*self.rong)
	# 3. Phuong thuc chuyen thong tin qua chuoi
	def toString(self):
		return (self.ten + "\t" +str(self.dai) + "\t" + str(self.rong) + "\t" + str(self.getChuVi()) + "\t" + str(self.getDienTich()))

# CHUONG TRINH CHINH
# 1. Khai bao 1 danh sach (mang)
DS = []

# 2. Nhap du lieu
n = input("Nhap vao so luong hinh chu nhat: ")
for i in range(n):
	print("--------------------")
	print("Hinh chu nhat thu " + str(i+1))
	Ten = raw_input("Nhap ten: ")
	CDai = input("Chieu dai: ")
	CRong = input("Chieu rong: ")
	DS.append(HCN(CDai,CRong,Ten))

# In danh sach hinh chu nhat
print("Danh dach hinh chu nhat vua nhap:")
print("TEN\tDAI\tRONG\tCHU VI\tDIEN TICH")
print("-----------------------------------------")
for item in DS:
	print(item.toString())
	print("\n")

# Tim hinh chu nhat co dien tich lon nhat
max_dt = DS[0].getDienTich()
max_ten = DS[0].getTen()
for item in DS:
	if (max_dt < DS[i].getDienTich()):
		max_dt = DS[i].getDienTich()
		max_ten = DS[i].getTen()

print("Hinh chu nhat co dien tich lon nhat la " + max_ten + ", co dien tich: " + str(max_dt))

# Xuat ra file
file = open('DanhSachHCN.txt','w+')
file.write("TEN\tDAI\tRONG\tCHU VI\tDIEN TICH\n")
for item in DS:
	file.write(item.toString()+"\n")






