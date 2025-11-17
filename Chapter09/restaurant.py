class Restaurant:
    def __init__(self, name, cuisine, location,rating):
        self.name = name
        self.cuisine = cuisine
        self.location = location
        self.rating = rating
    def describe_restaurant(self):
        print(f"{self.name}, a restaurant located in {self.location}, serves {self.cuisine} cuisine and has a rating of {self.rating}/5.")
    def open_restaurant(self):
        print(f"{self.name} is now open!")
    def increment_rating(self, increment):
        self.rating += increment
        return f"The new rating for {self.name} is {self.rating}/5.0."
    
gourmet = Restaurant("The Gourmet Kitchen", "Italian", "Capetown" , 4.5)
print(gourmet.open_restaurant())
print(gourmet.describe_restaurant())

shakeshack = Restaurant("Shake Shack", "Fast Food", "Johannesburg", 4.0)
print(shakeshack.open_restaurant())
print(shakeshack.describe_restaurant())

print(gourmet.increment_rating(0.1))
print(shakeshack.increment_rating(0.3))

KFC = Restaurant("KFC", "Fast Food", "London" ,2.0 )
print(KFC.open_restaurant())
print(KFC.describe_restaurant())
print(KFC.increment_rating(0.7))
