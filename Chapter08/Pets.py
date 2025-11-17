#Positional Arguments

def describe_pet(animal_type, pet_name):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('Jack', 'Cat')
describe_pet('dog', 'tom')

def describe_pets (animal_type,pet_name):
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pets (pet_name='tom', animal_type='dog')



