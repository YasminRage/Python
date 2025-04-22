motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']
motorcycles[1] = 'bmw'

print(motocycles) # ['ducati', 'bmw', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
# ['ducati', 'bmw', 'suzuki', 'ducati']

clothing_items = []
clothing_items.append('shirts')
clothing_items.append('pants')
clothing_items.append('shoes')
clothing_items.append('jackets')
print(clothing_items)
# ['shirts', 'pants', 'shoes', 'jackets']


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
print(popped_motorcycle) # suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.") 
# The last motorcycle I owned was a Suzuki.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# The first motorcycle I owned was a Honda.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)