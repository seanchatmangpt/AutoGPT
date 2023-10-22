# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("data.csv")

# Clean the data
data.dropna(inplace=True)

# Perform analytics
mean = np.mean(data)
median = np.median(data)
std = np.std(data)

# Visualize the results
plt.hist(data)
plt.title("Distribution of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)