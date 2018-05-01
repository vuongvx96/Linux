echo "------------------------------"
echo "--------- MENU DRINK ---------"
echo "------------------------------"

kq="Ban da chon: "
var1="Cafe den"
var2="Cafe da"
var3="Cafe sua"
var4="Cafe cao"

echo "1. " $var1
echo "2. " $var2
echo "3. " $var3
echo "4. " $var4

echo -e "\n"
read -p "Ban chon thuc uong nao (1-4): " ch
echo -n "Ban chon: "

case $ch in
"1")
	echo $var1;;
"2")
	echo $var2;;
"3")
	echo $var3;;
"4")
	echo $var4;;
*)
	clear
	echo "Lua chon khong phu hop";;
esac
