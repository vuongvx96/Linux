clear
if [ $# -ne 2 ]; then
	exit 0
else 
	num1=$1
	num2=$2
	echo "Tham so ban da truyen vao la 2 so: $num1 va $num2"
	echo "$num1 + $num2 = `expr $num1 + $num2`"
	echo "$num1 - $num2 = `expr $num1 - $num2`"
	echo "$num1 * $num2 = `expr $num1 \* $num2`"
	if test $num2 -eq 0; then
		echo "So chia bang 0 nen hok chia duoc"
	else
		echo "$num1 % $num2 = `expr $num1 % $num2`"
		echo "$num1 / $num2 = `expr $num1 + $num2`"
	fi
fi

