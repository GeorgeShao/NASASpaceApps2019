import os

def checkFileExists(file_name):
    if os.path.isfile(f'{file_name}'):
        print(f'File {file_name} exists')
        return True
    else:
        print(f'ERROR: File {file_name} does not exist')
        raise FileNotFoundError
        return False