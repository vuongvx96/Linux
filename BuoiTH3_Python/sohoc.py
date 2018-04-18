# Cac phep toan so hoc

a = float(input("Nhap vao so a: "))
b = input("Nhap vao so b: ")
oper = str(raw_input("Nhap vao phep toan (+, -, *, /, %): "))

if oper == "+":
   print("Ket qua cua %f + %f = %f " % (a,b,a+b))
elif oper == "-":
   print("Ket qua cua %f - %f = %f " % (a,b,a-b))
elif oper == "*":
   print("Ket qua cua %f * %f = %f " % (a,b,a*b))
elif oper == "/":
   print("Ket qua cua %f / %f = %f " % (a,b,a/b))
elif oper == "%":
   print("Ket qua cua %f - %f = %f " % (a,b,a%b))
elif oper == "**":
	print("Ket qua cua %f ^ %f = %f " % (a,b,a**b))
else:
   print("Phep toan ban nhap vao khong hop le!")

