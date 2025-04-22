# Creating class instance

my_new_car = ('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#modifying attribute values
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

 

my_leaf=ElectricCar('nissan','leaf',2020)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
