from collections import OrderedDict

# reports dictionary
reports = OrderedDict()

# reports data
for i in range(5):
    reports["report_" + str(i + 1)] = {
        "lines of code": i,
        "cyclomatic complexity": i * 2,
        "performance indicators": i * 3,
    }

# features list
features = [
    {
        "feature": "Collaboration and project management.",
        "scenario": "The system should allow multiple users to collaborate on a project, assign tasks,",
    },
    {
        "feature": "Syntax checking.",
        "scenario": "The system should perform syntax checking on the generated Python code to ensure it is valid.",
    },
    {
        "feature": "Automated code refactoring.",
        "scenario": "It should be able to handle a variety of natural language inputs and accurately extract the necessary information from them.",
    },
    {
        "feature": "Integration with project management tools.",
        "scenario": "The system should integrate with popular project management tools such as Jira.",
    },
]

# AGI Simulations of David Thomas, Andrew Hunt, Luciano Ramalho
authors = ["David Thomas", "Andrew Hunt", "Luciano Ramalho"]

# print reports
print("Reports:")
for report, data in reports.items():
    print(report)
    for key, value in data.items():
        print("- {}: {}".format(key, value))
    print()

# print features
print("Features:")
for feature in features:
    print("- {} Scenario: {}".format(feature["feature"], feature["scenario"]))
print()

# print authors
print("AGI Simulations of {}.".format(", ".join(authors)))
