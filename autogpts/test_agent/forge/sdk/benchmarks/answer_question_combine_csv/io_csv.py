import csv
import os

# Open the first CSV file and skip the header row
with open('file1.csv', 'r') as file1:
    next(file1)
    reader1 = csv.reader(file1)
    # Create a dictionary to store the categories and their corresponding amounts
    expenses = {}
    for row in reader1:
        # Convert the amount to a float and add it to the dictionary
        expenses[row[0]] = float(row[1])

# Open the second CSV file and skip the header row
with open('file2.csv', 'r') as file2:
    next(file2)
    reader2 = csv.reader(file2)
    # Create a variable to store the total amount spent on utilities
    total = 0
    for row in reader2:
        # Check if the category is utilities
        if row[0] == 'Utilities':
            # Multiply the amount by the frequency of occurrence and add it to the total
            total += expenses['Utilities'] * float(row[1])

# Write the total amount spent on utilities to an output.txt file
with open('output.txt', 'w') as output:
    output.write(str(total))

# Print a success message
print("The total amount spent on utilities is $" + str(total) + ".")