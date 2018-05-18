cars = 100# total cars
space_in_a_car = 4.0# capacity of each car
drivers = 30# total drivers
passengers = 90# total passengers
cars_not_driven = cars - drivers# total cars not driven
cars_driven = drivers# total cars driven
carpool_capacity = cars_driven * space_in_a_car# total capacity of driven cars
average_passengers_per_car = passengers / cars_driven# average passengers in driven cars

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
