import os
def read_directory_into_dict(directory_path):
    """
    Recursively reads a directory and its subdirectories into a nested dictionary structure.

    :param directory_path: The path to the directory to be read.
    :return: A nested dictionary where each key is a directory or file, 
             with directories mapping to another dictionary of their contents,
             and files mapping to None.
    """
    dir_dict = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            dir_dict[item] = read_directory_into_dict(item_path)
        else:
            dir_dict[item] = None
    return dir_dict