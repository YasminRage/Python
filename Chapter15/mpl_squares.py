import matplotlib.pyplot as plt
 
# Data for plotting
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Figure and an axes
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
input_values = [1, 2, 3, 4, 5]

# Plot the data
ax.plot(squares, marker='o', color='blue', linewidth=2)

# Add labels and title
ax.set_title("Yasmin's Graph", fontsize=18)
ax.set_xlabel("Index", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Show the plot
plt.show()
