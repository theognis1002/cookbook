"""
xargs - It converts input from standard input into arguments to a command.

example: 
files: hello_world.txt, test.txt README.md
"""
ls | HEAD -n2 | xargs -t
# Output: `echo hello_world.txt, test.txt`
