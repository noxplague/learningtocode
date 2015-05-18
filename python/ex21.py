def add(a, b,):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "can you do it by hand?"
# 25 + (74 - (180 * (50 / 2) ) )
# Formula for what = (a + b) - ( c * (d / 2))

equation_practice = (24 + 34) / (100 - 1023)

print equation_practice

equation_formula = divide(add(24, 34), subtract(100, 1023))

print equation_formula

a1 = float(raw_input("Give a value for a: ", ))
b1 = float(raw_input("Give a value for b: ", ))
c1 = float(raw_input("Give a value for c: ", ))
d1 = float(raw_input("Give a value for d: ", ))

what_formula = subtract(add(a1, b1), multiply(c1, divide(d1,2)))

print what_formula
