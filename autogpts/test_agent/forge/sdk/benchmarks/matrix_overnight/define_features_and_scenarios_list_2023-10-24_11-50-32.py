# Define a list of features, with each feature being a string
features = [
    "Real-time collaboration",
    "Task assignment",
    "Integration with external testing tools",
    "Automatic metrics and reports",
    "Database interaction code generation",
]

# Define a list of scenarios, with each scenario being a string
scenarios = [
    "Multiple users should be able to work on the same task simultaneously and see each other",
    "The Task Assignment Engine should assign tasks to team members based on their availability and skillset",
    "These reports should include information on execution time, memory usage, and any potential bottlenecks in the code",
    "These metrics and reports should include but are not limited to: code complexity, code coverage, and execution time analysis",
    "The system should generate Python code to interact with the database, including creating classes for each table",
]

# Define a list of authors, with each author being a string
authors = ["David Thomas", "Andrew Hunt", "Luciano Ramalho"]

# Define a dictionary to store information about the authors
authors_info = {
    "David Thomas": {
        "name": "David Thomas",
        "country": "USA",
        "occupation": "Software Engineer",
    },
    "Andrew Hunt": {
        "name": "Andrew Hunt",
        "country": "USA",
        "occupation": "Software Engineer",
    },
    "Luciano Ramalho": {
        "name": "Luciano Ramalho",
        "country": "Brazil",
        "occupation": "Software Engineer",
    },
}


# Define a function to print the information of each author
def print_author_info(author):
    print("Name: {}".format(author["name"]))
    print("Country: {}".format(author["country"]))
    print("Occupation: {}".format(author["occupation"]))
    print()


# Print the information of each author in the dictionary
for author_name in authors:
    author = authors_info[author_name]
    print_author_info(author)
