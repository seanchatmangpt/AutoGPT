# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt


# Define function to load and clean data
def load_data(file_path):
    """
    Loads data from given file path and cleans it by removing null values and duplicates.

    Args:
        file_path (str): Path to data file.

    Returns:
        df (pandas.DataFrame): Cleaned data in a pandas DataFrame.
    """
    # Load data into DataFrame
    df = pd.read_csv(file_path)

    # Remove null values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    return df


# Define function to plot data
def plot_data(df, x_col, y_col):
    """
    Plots data from given DataFrame using specified columns as x and y axes.

    Args:
        df (pandas.DataFrame): Data to be plotted.
        x_col (str): Column to be used as x axis.
        y_col (str): Column to be used as y axis.
    """
    # Create plot
    plt.plot(df[x_col], df[y_col])

    # Add labels and title
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title("Data Plot")

    # Show plot
    plt.show()


# Load and clean data
df = load_data("data.csv")

# Plot data
plot_data(df, "x", "y")
