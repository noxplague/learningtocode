# all of these variables are being created and given values
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# these variables are being given values based on earlier variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# This is combine the text with the value of cars variable
print "There are", cars, "cars available."

# This will combine the text with the value of drivers variable
print "There are only", drivers, "drivers available."

# this will print the text and the cars not driven variable
print "There will be", cars_not_driven, "empty cars today."

#this will print text plus the carpool capacity variable
print "We can transport", carpool_capacity, "people today."

# This will print the passengers traveling
print "We have", passengers, "to carpool today."

# This will print the average passengers per car variable
print "We need to put about", average_passengers_per_car, "in each car."