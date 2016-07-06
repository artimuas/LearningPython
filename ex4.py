cars = 100
space_in_a_car = 4.0
drivers = 35
passengers = 200
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print "There are ",cars," cars available"
print "There are only ", drivers, "drivers available"
print cars_not_driven, "cars are not driven"
print "Each car can carry ", carpool_capacity, "passengers"
