import matplotlib.pyplot as plt

# Data for plotting
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Define the x/y for scatter
x_values = input_values

y_values = squares

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

# Line plot
ax.plot(x_values, y_values, marker='o', color='blue', linewidth=3)

# Scatter plot
ax.scatter(x_values, y_values, color='red', s=50)

# Labels and title
ax.set_title("Yasmin's Graph", fontsize=18)
ax.set_xlabel("Index", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Ticks
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

# Show plot
plt.show()

# Save AFTER plt.show()
fig.savefig('squares_plot.png', bbox_inches='tight')
