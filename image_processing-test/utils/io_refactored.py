
# io.py

def read_file(file_path):
    """
    Reads data from a file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    list of str: The lines read from the file.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def write_file(file_path, data):
    """
    Writes data to a file.

    Parameters:
    file_path (str): The path to the file.
    data (list of str): The lines to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.writelines(data)
