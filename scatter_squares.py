

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)

#Set chart title and label axis
ax.set_title("Square Numbers", fontsize=16)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Square of Value", fontsize=10)

ax.tick_params(axis='both', which='major', labelsize=10)

#Set range for each axis: 
ax.axis([0,1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

