# Creates function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
# Calls the function with two arguments	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# Creates variables with hardcoded values
print "OR, we can use varaibles from our script:"
amount_of_cheese = 10
amount_of_crackers= 50
# Runs the function with those variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Calls the function with math inside for the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# Combines the variables with math as the arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
