class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):  
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

#child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2020)
print(my_leaf.get_descriptive_name())
