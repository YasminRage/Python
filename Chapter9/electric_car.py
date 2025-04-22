class ElectricCar(ecar)
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        

my_leaf=ElectricCar('nissan','leaf',2020)
print(my_leaf.get_descriptive_name())