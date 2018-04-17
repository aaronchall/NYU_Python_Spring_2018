import os
import pprint

def get_PATH_environment_variable():
    """returns the PATH environment variable, or '' if not there"""
    return os.getenv('PATH', default='')

def get_PATH_list():
    return get_PATH_environment_variable().split(os.pathsep)

def main():
    pprint.pprint(get_PATH_list())
    
if __name__ == '__main__':
    main()
