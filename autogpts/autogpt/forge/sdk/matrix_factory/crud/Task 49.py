# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("test_data.csv")

# Clean the data
data.dropna(inplace=True)

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std = np.std(data)

# Visualize the data
plt.plot(data)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Test Data")
plt.show()

# Print the results
print("Mean:", mean)
print("Standard Deviation:", std)