# Given data
x_values = [1, 2, 3, 4, 5, 6]
y_values = [101, 111, 122, 133, 144, 155]
learning_rate = 0.04

# Initial estimates
old_intercept = 50
old_slope = 0.2


# Calculate the partial derivatives for the update rules
partial_derivative_intercept = -2 * sum(y_i - (old_slope * x_i + old_intercept) for x_i, y_i in zip(x_values, y_values)) / len(x_values)
partial_derivative_slope = -2 * sum(x_i * (y_i - (old_slope * x_i + old_intercept)) for x_i, y_i in zip(x_values, y_values)) / len(x_values)

# Update the intercept and slope
new_intercept = old_intercept - learning_rate * partial_derivative_intercept
new_slope = old_slope - learning_rate * partial_derivative_slope

# Display the results
print("Old Intercept:", old_intercept)
print("Old Slope:", old_slope)
print("New Intercept:", new_intercept)
print("New Slope:", new_slope)