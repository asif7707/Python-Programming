import numpy as np

# Create a 5x5 matrix
matrix = np.array([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]])

# Find the position of the 1 value
position = np.where(matrix == 1)

# Print the position
print(position)
print(position[0][0], position[1][0])
