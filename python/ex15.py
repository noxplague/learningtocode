# from the sys module this imports the argv feature
from sys import argv
# assigns variables to the argv
script, filename, = argv
# assigns the open command to a variable
txt = open(filename)
# Prints the filename being opened, 
# and takes the file given from open and runs the command read
# without any parameters
print "Here's your file %r:" % filename
print txt.read()
# This sections does the identical actions, but gets the value from the user
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()