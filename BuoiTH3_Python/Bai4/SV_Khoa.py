class SinhVien:
	"""docstring for SinhVien"""
	MSSV = "",
	HoTen = "",
	MaKhoa = ""
	def __init__(self, mssv, hoten, makhoa):
		self.MSSV = mssv
		self.HoTen = hoten
		self.MaKhoa = makhoa

	def getMSSV(self):
		return self.MSSV
	def setMSSV(self,mssv):
		self.MSSV = mssv
	def getHoTen(self):
		return self.HoTen
	def setHoTen(self,hoten):
		self.HoTen = hoten
	def getMaKhoa(self):
		return self.MaKhoa
	def setMaKhoa(self,makhoa):
		self.MaKhoa = makhoa
	# Phuong thuc xuat thong tin mot sinh vien
	def XuatTT(self):
		print("MSSV: " + self.MSSV + "\tHo ten: " + self.HoTen + "\tMa khoa: " + self.MaKhoa)
		

class Khoa:
	"""docstring for Khoa"""
	MaKhoa = "",
	TenKhoa = ""
	def __init__(self, makhoa, tenkhoa):
		self.MaKhoa = makhoa
		self.TenKhoa = tenkhoa
	def getMaKhoa(self):
		return self.MaKhoa
	def setMaKhoa(self,makhoa):
		self.MaKhoa = makhoa
	def getTenKhoa(self):
		return self.TenKhoa
	def setTenKhoa(self,tenkhoa):
		self.TenKhoa = tenkhoa
	def Xuat(self):
		print("Ma khoa: " + self.MaKhoa + "\t Ten khoa: " + self.TenKhoa)