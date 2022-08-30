# Does file or directory exist?
if [ -e /file/to/test.txt ]
then
  echo "Exists"
fi

# Is file a directory?
if [ -d /file/to/test ]
then
  echo "Yes, directory"
fi

# Compare two strings
[ string1 == string2 ]
[ string1 != string2 ]
[ string1 < string2 ]
[ string1 > string2 ]

# And
[ expr1 -a expr2 ]
# Or
[ expr1 -o expr2 ]
# Not
[ !expr1 ]

# Arithmetic 
# equal, not equal, less than, less equal, greather than, greater equal
-eq, -ne, -lt, -le, -gt, -ge



# Example 1

read x
read y

if [ $x -gt $y ]
then
echo X is greater than Y
elif [ $x -lt $y ]
then
echo X is less than Y
elif [ $x -eq $y ]
then
echo X is equal to Y
fi


# Example 2

read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then 
echo ISOSCELES
else
echo SCALENE

fi
