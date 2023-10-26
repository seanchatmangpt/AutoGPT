# 1. Write a function that takes a list of strings and returns a list of the same strings, but in lowercase.

def lowercase_list(string_list):
    return [string.lower() for string in string_list]


# 2. Write a function that takes a list of numbers and returns a new list where each element is multiplied by 2.

def multiply_by_two(num_list):
    return [num * 2 for num in num_list]


# 3. Write a function that takes a string and returns a new string with all leading and trailing whitespace removed.

def strip_whitespace(string):
    return string.strip()


# 4. Write a function that takes a list of numbers and returns the sum of all the numbers in the list.

def sum_numbers(num_list):
    return sum(num_list)


# 5. Write a function that takes a list of strings and returns a new list with only the strings that have a length greater than 5.

def filter_long_strings(string_list):
    return [string for string in string_list if len(string) > 5]


# 6. Write a function that takes a list of numbers and returns the maximum number in the list.

def find_max(num_list):
    return max(num_list)


# 7. Write a function that takes a list of strings and returns a new list with the strings reversed.

def reverse_strings(string_list):
    return [string[::-1] for string in string_list]


# 8. Write a function that takes a list of strings and returns a new list with only the strings that contain a specific character.

def filter_strings(string_list, character):
    return [string for string in string_list if character in string]


# 9. Write a function that takes a list of strings and returns a new list with the strings sorted alphabetically.

def sort_strings(string_list):
    return sorted(string_list)


# 10. Write a function that takes a list of strings and returns a new list with the strings sorted by length, longest to shortest.

def sort_strings_by_length(string_list):
    return sorted(string_list, key=len, reverse=True)