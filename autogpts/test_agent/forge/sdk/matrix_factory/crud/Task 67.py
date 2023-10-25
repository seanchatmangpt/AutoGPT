# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the test data
test_data = pd.read_csv("test_data.csv")

# Use Seaborn to create a scatter plot
sns.scatterplot(x="x_values", y="y_values", data=test_data)

# Add labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Test Data Visualization")

# Show the plot
plt.show()
