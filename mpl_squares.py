import matplotlib.pyplot as plt

# values = [ i for i in range(100)]
squares = [x**2 for x in range(100)]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()