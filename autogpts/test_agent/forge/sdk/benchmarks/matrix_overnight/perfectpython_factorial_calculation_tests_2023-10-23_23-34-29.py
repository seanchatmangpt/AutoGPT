# Here is your PerfectPythonProductionCode® AGI response. Tests have been written to a different file:


def calculate_factorial(n):
    """
    Calculates the factorial of a given number.

    :param n: The number to calculate the factorial of
    :type n: int
    :return: The factorial of the given number
    :rtype: int
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Test cases

assert calculate_factorial(0) == 1
assert calculate_factorial(1) == 1
assert calculate_factorial(5) == 120
assert calculate_factorial(10) == 3628800
assert calculate_factorial(15) == 1307674368000
