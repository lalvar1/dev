# print odd numbers
for number in {1..99..2}
do
    echo $number
done


# opeartions
read x
read y
echo "$((x+y))"
echo "$((x-y))"
echo "$((x*y))"
echo "$((x/y))"

# over same line
read input
result=$(echo "$input" | bc -l)
printf "%.3f" $result


# comparison
read firstNumber
read secondNumber
if (($firstNumber > $secondNumber)); then
    echo X is greater than Y;
elif (($firstNumber < $secondNumber)); then
    echo X is less than Y;
else
    echo X is equal to Y;
fi

# conditionals
read x
if [[ $x == "y" || $x == "Y" ]]; then echo "YES"
else echo "NO"
fi

read x
read y
read z
if [ $x -eq $y ] && [ $x  -eq $z ];then echo "EQUILATERAL";
elif [ $x -eq $y ] || [ $x -eq $z ] || [ $y -eq $z ]; then echo "ISOSCELES";
else echo "SCALENE";
fi

# average calculation
read n  # number of lines
sum=0
for ((i=0;i<$n;i++))
do
    read temp
    sum=$(awk "BEGIN {print $sum+$temp; exit}")
done
result=$(echo "$sum/$n" | bc -l)
printf "%.3f\n" $result

# Read array
array=($(cat))
echo ${array[@]}

# Replace capital letter for '.'
readarray array
echo ${array[@]/[A-Z]/.}

# Slice from pos 3 to 7
echo ${array[@]:3:5}
# Get index 3
echo ${array[3]}

# get 3rd char from lines
cut -c3
# get last 20 lines from file
tail -n20
# read from line 12 to 22
head -n22 | tail -n11
head -22 | tail -11

# traslation
tr "()" "[]"

# check for column in file
awk '{if ($4 == "") print "Not all scores are available for",$1;}'

# Replace in file the with this
sed 's/the /this /'

# count lines
wc -l

