#!/bin/bash
# Nhap ho ten kiem tra dung thi xuat

read -p 'Nhap ho: ' lastName

read -p 'Nhap ten: ' firstName

# ${string,,} de lowercase chuoi

if [[ ${lastName,,} = "vo xuan" && ${firstName,,} = "vuong" ]]; then
	echo "Trung khop"
else
	echo "Khong trung khop"
fi


