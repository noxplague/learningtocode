# Creating joke variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Using the variable strings inside another string variable
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# Printing the variables inside another string, using format characters to reference
print "I said: %r." % x
print "I also said: '%s'." % y
# Assigning a boolean variable, also Joke eval has a format
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# Printing the joke eval assigning a value to the formatting character at this time
print joke_evaluation % hilarious
# Adding strings together
w = "This is the left side of..."
e = "a string with a right side."

print w + e