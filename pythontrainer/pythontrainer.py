import builtins
import string

def list_builtins():
    """list_builtins with list comprehension!!!"""
    return [n for n in dir(builtins) if n[0] in string.ascii_lowercase]

def api(obj):
    """list the Application Programming Interface of an object"""
    return [n for n in dir(obj) if n[0] != '_']
