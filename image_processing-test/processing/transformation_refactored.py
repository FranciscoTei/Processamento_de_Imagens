
# transformation.py

def double_data(data_list):
    """
    Doubles each element in the list.

    Parameters:
    data_list (list of numeric): The list of values to be doubled.

    Returns:
    list of numeric: A new list with each element doubled.
    """
    return [element * 2 for element in data_list]

def halve_data(data_list):
    """
    Halves each element in the list.

    Parameters:
    data_list (list of numeric): The list of values to be halved.

    Returns:
    list of numeric: A new list with each element halved.
    """
    return [element / 2 for element in data_list]
