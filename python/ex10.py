tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\\"
print "\'"
print "\""
print "\a"
print "\b"
print "\f"
print "\n"
print "\N{name}"
print "\r"
print "\t"
print "\v"
print "\ooo"
print "\hxx"

print "%r" % "\""
print "%r" % "\'"
print "%s" % "\""
print "%s" % "\'"

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,