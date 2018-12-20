

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


print(slope(-4, 1, 0, 0))

# Define the known points
x = [-4, 0]
y = [1, 0]

# Calculate the coefficients. This line answers the initial question.
coefficients = np.polyfit(x, y, 1)

# Print the findings
print('a =', coefficients[0])
print('b =', coefficients[1])

# Let's compute the values of the line...
polynomial = np.poly1d(coefficients)
x_axis = np.linspace(0, 500, 100)
y_axis = polynomial(x_axis)

# ...and plot the points and the line
plt.plot(x_axis, y_axis)
plt.plot(x[0], y[0], 'go')
plt.plot(x[1], y[1], 'go')
plt.grid('on')
plt.show()

# points = [(-4, 1), (0, 0)]
# x_coords, y_coords = zip(*points)
# A = vstack([x_coords, ones(len(x_coords))]).T
# m, c = lstsq(A, y_coords)[0]
# print("Line Solution is y = {m}x + {c}".format(m=m, c=c))