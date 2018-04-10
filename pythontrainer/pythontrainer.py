import builtins
import string

BUILTINS_DATA = {
    'io': [print, input, open,],
    'introspection': [
        dir, type, id, hash,
        isinstance, issubclass, callable,
        help, len, vars,
    ],
    'types': [
        object, type,
        int, bool, float, complex,
        str, bytes,
        tuple, list,
        frozenset, set,
        dict,],
    'iteration':[
        range, enumerate, zip,
        map, filter, # we prefer list comprehensions
        iter, next,
        slice, reversed,
    ],
    'OOP': [
        staticmethod, classmethod,
        property,
        delattr, setattr, getattr,
    ],
    'math': [
        abs, all, any,
        bin,hex, oct,
        pow, round,
        sum,
    ],
}

def list_builtins():
    """list_builtins with list comprehension!!!"""
    return [n for n in dir(builtins) if n[0] in string.ascii_lowercase]

def api(obj):
    """list the Application Programming Interface of an object"""
    return [n for n in dir(obj) if n[0] != '_']

def create_obscured_doc(obj, name):
    """given obj with a name, return obscured doc"""
    return obj.__doc__.replace(name, '*'*len(name))
