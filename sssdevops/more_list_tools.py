"""
More list manipulations
"""


def split(in_list, index):
    """

    Parameters
    ----------
    in_list: list
    index: int

    Returns
    -------
    Two lists, spliting in_list by 'index'

    Examples
    -------
    >>> split(['a', 'b', 'c', 'd'], 3)
    (['a', 'b', 'c'], ['d'])
    """

    list1 = in_list[:index]
    list2 = in_list[index:]

    return list1, list2
