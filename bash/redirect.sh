# 0 = stdin
# 1 = stdout
# 2 = stderr

echo "Output #1" 1>&2 # redirect stdout to stderr
echo "Output #2" 1>/dev/null  # redirect stdout to /dev/null (squlech)

echo "New file" > new_file.txt  # redirects output to file

# animals.txt
"""cow
lion
bird
dog
zebra
antelope"""

ECHO "panda" >> animals.txt # The append >> operator adds the output to the existing content instead of overwriting it.

sort < animals.txt  # The input redirector pulls data in a stream from a given source.
"""
Output:
antelope
bird
cow
dog
lion
panda
zebra
"""
