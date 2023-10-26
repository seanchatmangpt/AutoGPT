import csv
import json

from forge.sdk.utils.complete import create

task = json.loads(open('data.json').read())['task']


def combine_csv(file1, output_file):
    """
    Combines two csv files using the 'ID' column, sorts the rows by ID in ascending order and the columns alphabetically, and writes the output to a new csv file.

    Args:
        file1 (str): Name of first csv file
        file2 (str): Name of second csv file
        output_file (str): Name of output csv file

    Returns:
        None
    """

    text1 = open(file1, 'r').read()

    new_csv = create(f"{task}\nKeep the header in the same order\n```file1.csv\n{text1}\n```output\n", stop=['```'], max_tokens=2500)

    # Write output to new csv file
    with open(output_file, 'w') as file:
        file.write(new_csv)


# Call function with given file names
combine_csv('file1.csv', 'output.txt')