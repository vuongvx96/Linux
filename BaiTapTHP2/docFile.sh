#!/bin/sh
echo -e "nhap ten file:"
read filename

if [ ! -f "$filename" ]; then
	echo " $filename not exists"
	exit 1
fi
answer=""
count=0
numlines=`cat $filename | sed '/\/\//d' | sed '/^\s*$/d' | wc -l`
echo “ so dong: $numlines”
while [ "$answer"!="n" ]
do
	echo -e "tiep tuc(y/n)?"
	read answer
	if [ "answer" = "y" ]; then
		echo "doc het file rui"
		exit 0
	fi
	count=$(($count+1))
	sed –n ${count}p $filename
done
exit 0
