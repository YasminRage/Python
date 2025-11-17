# Store information about a pizza being ordered.
pizza = {
'order_number': '526',
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese', 'pepperoni'],
}
# Summarize the order.
print(f"Hello, you ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
 print(f"\t{topping}")


print(f"your order number is {pizza['order_number']}")







