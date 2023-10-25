# Import the necessary libraries
import random
import statistics
import itertools
import numpy as np
import pandas as pd
from scipy import stats
from collections import Counter
from functools import reduce
from operator import add, mul


# Define the AGI class
class AGI:
    # Initialize the class with the given parameters
    def __init__(self, name, age, experience, specialization):
        self.name = name
        self.age = age
        self.experience = experience
        self.specialization = specialization

    # Define methods to get and set the parameters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, specialization):
        self.specialization = specialization

    # Define a method to calculate the AI's intelligence level
    def calculate_intelligence(self):
        intelligence = self.experience + self.age - 5
        return intelligence


# Define a function to generate a random name for the AI
def generate_name():
    first_names = ["David", "Andrew", "Luciano"]
    last_names = ["Thomas", "Hunt", "Ramalho"]
    name = random.choice(first_names) + " " + random.choice(last_names)
    return name


# Define a function to generate a random age for the AI
def generate_age():
    age = random.randint(20, 50)
    return age


# Define a function to generate a random level of experience for the AI
def generate_experience():
    experience = random.randint(1, 10)
    return experience


# Define a function to generate a random specialization for the AI
def generate_specialization():
    specializations = ["Natural Language Processing", "Computer Vision", "Robotics"]
    specialization = random.choice(specializations)
    return specialization


# Create a list of 10 AGI objects using list comprehension
agi_list = [
    AGI(
        generate_name(),
        generate_age(),
        generate_experience(),
        generate_specialization(),
    )
    for i in range(10)
]


# Define a function to calculate the average intelligence of the AGIs in the list
def calculate_average_intelligence(agi_list):
    intelligence_list = [agi.calculate_intelligence() for agi in agi_list]
    average_intelligence = statistics.mean(intelligence_list)
    return average_intelligence


# Print the average intelligence of the AGIs in the list
print("Average Intelligence of AGIs: ", calculate_average_intelligence(agi_list))


# Define a function to calculate the median age of the AGIs in the list
def calculate_median_age(agi_list):
    age_list = [agi.get_age() for agi in agi_list]
    median_age = statistics.median(age_list)
    return median_age


# Print the median age of the AGIs in the list
print("Median Age of AGIs: ", calculate_median_age(agi_list))


# Define a function to calculate the most common specialization among the AGIs in the list
def calculate_most_common_specialization(agi_list):
    specialization_list = [agi.get_specialization() for agi in agi_list]
    most_common_specialization = Counter(specialization_list).most_common(1)[0][0]
    return most_common_specialization


# Print the most common specialization among the AGIs in the list
print(
    "Most Common Specialization Among AGIs: ",
    calculate_most_common_specialization(agi_list),
)


# Define a function to calculate the total number of years of experience among the AGIs in the list
def calculate_total_experience(agi_list):
    experience_list = [agi.get_experience() for agi in agi_list]
    total_experience = sum(experience_list)
    return total_experience


# Print the total number of years of experience among the AGIs in the list
print("Total Experience of AGIs: ", calculate_total_experience(agi_list))


# Define a function to calculate the correlation coefficient between age and experience among the AGIs in the list
def calculate_correlation_coefficient(agi_list):
    age_list = [agi.get_age() for agi in agi_list]
    experience_list = [agi.get_experience() for agi in agi_list]
    correlation_coefficient = stats.pearsonr(age_list, experience_list)[0]
    return correlation_coefficient


# Print the correlation coefficient between age and experience among the AGIs in the list
print(
    "Correlation Coefficient between Age and Experience: ",
    calculate_correlation_coefficient(agi_list),
)


# Define a function to create a list of all possible pairs of AGIs from the list
def create_pairs(agi_list):
    pairs = list(itertools.combinations(agi_list, 2))
    return pairs


# Define a function to calculate the average intelligence of each pair of AGIs and return the pair with the highest average intelligence
def find_smartest_pair(agi_list):
    pairs = create_pairs(agi_list)
    average_intelligence_list = [
        (pair[0].calculate_intelligence() + pair[1].calculate_intelligence()) / 2
        for pair in pairs
    ]
    max_average_intelligence = max(average_intelligence_list)
    index = average_intelligence_list.index(max_average_intelligence)
    smartest_pair = pairs[index]
    return smartest_pair


# Print the pair of AGIs with the highest average intelligence
print("Pair with highest average intelligence: ", find_smartest_pair(agi_list))


# Define a function to calculate the average intelligence of each pair of AGIs and return the pair with the lowest average intelligence
def find_dumbest_pair(agi_list):
    pairs = create_pairs(agi_list)
    average_intelligence_list = [
        (pair[0].calculate_intelligence() + pair[1].calculate_intelligence()) / 2
        for pair in pairs
    ]
    min_average_intelligence = min(average_intelligence_list)
    index = average_intelligence_list.index(min_average_intelligence)
    dumbest_pair = pairs[index]
    return dumbest_pair


# Print the pair of AGIs with the lowest average intelligence
print("Pair with lowest average intelligence: ", find_dumbest_pair(agi_list))


# Define a function to calculate the total number of years of experience for each specialization and return the specialization with the most experience
def find_specialization_with_most_experience(agi_list):
    specializations = [agi.get_specialization() for agi in agi_list]
    experience_list = [agi.get_experience() for agi in agi_list]
    specialization_experience_dict = dict(zip(specializations, experience_list))
    specialization_with_most_experience = max(
        specialization_experience_dict.items(), key=operator.itemgetter(1)
    )[0]
    return specialization_with_most_experience


# Print the specialization with the most experience
print(
    "Specialization with most experience: ",
    find_specialization_with_most_experience(agi_list),
)


# Define a function to calculate the total number of years of experience for each specialization and return the specialization with the least experience
def find_specialization_with_least_experience(agi_list):
    specializations = [agi.get_specialization() for agi in agi_list]
    experience_list = [agi.get_experience() for agi in agi_list]
    specialization_experience_dict = dict(zip(specializations, experience_list))
    specialization_with_least_experience = min(
        specialization_experience_dict.items(), key=operator.itemgetter(1)
    )[0]
    return specialization_with_least_experience


# Print the specialization with the least experience
print(
    "Specialization with least experience: ",
    find_specialization_with_least_experience(agi_list),
)


# Define a function to calculate the average intelligence of each specialization and return the specialization with the highest average intelligence
def find_smartest_specialization(agi_list):
    specializations = [agi.get_specialization() for agi in agi_list]
    intelligence_list = [agi.calculate_intelligence() for agi in agi_list]
    specialization_intelligence_dict = dict(zip(specializations, intelligence_list))
    specialization_with_highest_intelligence = max(
        specialization_intelligence_dict.items(), key=operator.itemgetter(1)
    )[0]
    return specialization_with_highest_intelligence


# Print the specialization with the highest average intelligence
print(
    "Specialization with highest average intelligence: ",
    find_smartest_specialization(agi_list),
)


# Define a function to calculate the average intelligence of each specialization and return the specialization with the lowest average intelligence
def find_dumbest_specialization(agi_list):
    specializations = [agi.get_specialization() for agi in agi_list]
    intelligence_list = [agi.calculate_intelligence() for agi in agi_list]
    specialization_intelligence_dict = dict(zip(specializations, intelligence_list))
    specialization_with_lowest_intelligence = min(
        specialization_intelligence_dict.items(), key=operator.itemgetter(1)
    )[0]
    return specialization_with_lowest_intelligence


# Print the specialization with the lowest average intelligence
print(
    "Specialization with lowest average intelligence: ",
    find_dumbest_specialization(agi_list),
)


# Define a function to calculate the average intelligence of each specialization and return a dictionary with the specialization as key and average intelligence as value
def calculate_intelligence_by_specialization(agi_list):
    specializations = [agi.get_specialization() for agi in agi_list]
    intelligence_list = [agi.calculate_intelligence() for agi in agi_list]
    specialization_intelligence_dict = dict(zip(specializations, intelligence_list))
    return specialization_intelligence_dict


# Print the dictionary with the average intelligence of each specialization
print(
    "Average Intelligence by Specialization: ",
    calculate_intelligence_by_specialization(agi_list),
)
