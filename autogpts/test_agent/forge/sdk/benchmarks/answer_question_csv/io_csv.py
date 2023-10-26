import csv

def calculate_total_utility_expenses(csv_file):
    """
    Calculates the total amount spent on utilities and writes the answer to an output.txt file.

    Args:
        csv_file (str): Path to the CSV file containing the expenses data.

    Returns:
        float: Total amount spent on utilities.
    """
    total = 0.0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader) # skip header row
        for row in reader:
            if row[3] == 'Utilities':
                total += float(row[2])
    with open('output.txt', 'w') as file:
        file.write(str(total))
    return total

# Example usage:
print(calculate_total_utility_expenses('file1.csv'))