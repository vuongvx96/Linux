echo "---------------------"
echo "--- CAC PHEP TOAN ---"
echo "_____________________"

var1="+"
var2="-"
var3="*"
var4="/"

echo "Cong: +"
echo "Tru: -"
echo "Nhan: *"
echo "Chia: /"
echo "Ket thuc (q)"
echo 
read -p "Chon phep toan: " oper
if [[ ${oper,,} = "q" ]]; then
	exit 0
fi 

echo -n "Nhap so thu nhat: "
read a
echo -n "Nhap so thu hai: "
read b

kq=0;
case $oper in
"+")
	let "kq=$a+$b";;
"-")
	let "kq=$a-$b";;
"*")
	let "kq=$a*$b";;
"/")
	let "kq=$a/$b";;
*)
	echo "Lua chon khong dung"
	sleep 5;;
esac 
echo
echo "Ket qua cua $a $oper $b = $kq"
	 

