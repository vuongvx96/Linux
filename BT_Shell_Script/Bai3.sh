gio=$(date +"%H")
echo -e "Bay gio la $gio gio"

if [ 1 -ge $gio -a $gio -le 10 ] 
then
	echo "Chao buoi sang"
elif [ 11 -ge $gio -a $gio -lt 13 ]
then
	echo "Chao buoi trua"
elif [13 -ge $gio -a $gio -lt 17 ]
then
	echo "Chao buoi chieu"
else
	echo "Chao buoi toi"
fi


