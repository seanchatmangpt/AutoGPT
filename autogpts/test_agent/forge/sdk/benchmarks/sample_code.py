# sample_code.py


def three_sum(nums, target):
    """
    Given an array of integers, return indices of the three numbers such that they add up to a specific target.
    :param nums: list of integers
    :param target: integer
    :return: list of indices
    """
    # create a dictionary to store the complement of each number in the list
    complement_dict = {}

    # loop through the list of numbers
    for i, num in enumerate(nums):
        # check if the complement of the current number is in the dictionary
        if target - num in complement_dict:
            # if it is, return the indices of the two numbers that add up to the target
            return [complement_dict[target - num], i]
        else:
            # if not, add the current number and its index to the dictionary
            complement_dict[num] = i

    # if no solution is found, return an empty list
    return []
