import os
from os import path
from pathlib import Path

class InputError(Exception):
    pass

def countfiles(directory):
    '''
        This function returns the total number of files in a directory and sub-directory.
    '''
    number_of_files = 0
    if path.isdir(directory) == False:
        raise InputError('countfile accepts only directory')
    with os.scandir(directory) as contents:
        for content in contents:
            content_path = Path(content)
            if path.isdir(content_path):
                number_of_files += countfiles(content_path)
            else:
                number_of_files += 1
    return number_of_files
    

if __name__ == '__main__':
    pass
