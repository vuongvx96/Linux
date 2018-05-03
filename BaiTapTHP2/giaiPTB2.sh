#!/bin/bash
echo -n "a= "
read a
echo -n "b= "
read b
echo -n "c= "
read c
delta=$(echo "$b^2 - 4*$a*$c" | bc)
if [ $delta -lt 0 ]
then
	echo "pt vo nghiem"
elif [ "$delta" -eq 0 ]
then
	echo -n "pt co nghiem kep x= "
	x=$(echo "scale=2; -$b/(2*$a)" | bc)
	echo "$x"
else
	echo "phuong trinh co 2 nghiem"
	x1=$(echo "scale=2; -($b + sqrt($delta))/(2*$a)" | bc)
echo "x1= $x1"
	x2=$(echo "scale=2; -($b - sqrt($delta))/(2*$a)" | bc)
echo "x2= $x2"
	fi
exit 0
