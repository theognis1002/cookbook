# Run the last command again
!!

# Check history
history

# Run specific history command
!319

# Repeat the last command but replace something
^searchString^replaceString^

# Equivalent search/replace last command
``!!:s/searchString/replaceString/''

# Globally search replace the previous command
!!:gs/old/new/

# History tricks
make a directory then move into it:
mkdir cgi-bin; cd !#$ 
!#$ is shorthand for "the first word of this command". If I wanted to pick the third word
out of the previous command, that would be: !!:3 (don't forget there is a zeroth word).

# Run the last command that contained string
!?string

# Search history with CTRL-R