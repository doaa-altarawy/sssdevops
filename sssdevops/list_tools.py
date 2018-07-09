"""
Main python file for the sssdevops example
"""

# import statements go here


def mean(num_list):
    """
    Calculate the mean of a list of numbers

    Parameters
    ----------
    num_list: list of int or float

    Returns
    -------
    float of the mean of the list

    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    return sum(num_list) / len(num_list)
