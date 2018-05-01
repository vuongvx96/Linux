if [ $# -ne 2 ]; then
	exit 0
else
	for((i = 1;i <= $2; i++))
	do
		echo $1;
	done
fi
