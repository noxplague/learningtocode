print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
# Using %r will give you the height with a \ to prevent string breaking
print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)