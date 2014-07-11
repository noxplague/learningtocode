def open_and_edit(file):
	
	editing = open(file, 'w')
	editing.truncate()
	
	print "Now what would you like to write? "
	line1 = raw_input("line 1: ") + "\n"
	line2 = raw_input("line 2: ") + "\n"
	line3 = raw_input("line 3: ") + "\n"
	
	editing.write(line1 + line2 + line3)
	editing.close
	
filename = raw_input("Please enter the file name you'd like to edit: ", )
open_and_edit(filename)

print "Lets confirm what you just wrote: "

read_back = open(filename)

print read_back.read()