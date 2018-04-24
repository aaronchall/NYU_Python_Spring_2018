"""This is the Python Trainer Module"""

import builtins
import string
import random
import time

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
        bin, hex, oct,
        pow, round,
        sum,
    ],
}

CATEGORIES = dict(builtins=BUILTINS_DATA)

def list_builtins() -> list:
    """list_builtins with list comprehension!!!

    >>> list_builtins()
    ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

    >>> set_of_builtins = {'abs', 'all', 'any', 'ascii', 'bin'}
    >>> set_of_builtins.issubset(list_builtins())
    True
    """
    return [n for n in dir(builtins) if n[0] in string.ascii_lowercase]

def api(obj):
    """list the Application Programming Interface of an object"""
    return [n for n in dir(obj) if n[0] != '_']

def create_obscured_doc(obj, name):
    """given obj with a name, return obscured doc"""
    return obj.__doc__.replace(name, '*'*len(name))

def short_fn_doc(function):
    """given a function, return the first 20 lines of its documentation"""
    doc = create_obscured_doc(function, function.__name__)
    lines = doc.splitlines(True)[:20]
    return ''.join(lines)

def list_objs_to_dict(list_of_objs):
    """given a list of named objects, return dict of names to objects"""
    return {obj.__name__: obj for obj in list_of_objs}

def list_of_methods(a_type):
    """given a type return a list of its public (actual) methods"""
    type_api = api(a_type)
    return [method for name, method in vars(a_type).items() if name in type_api]

def select_category():
    """prompt a user to select a catagory"""
    print('Please input a category (Ctrl-C to exit):')
    print(', '.join(CATEGORIES.keys()))
    input_taken = input('> ')
    return input_taken

def select_builtin_category():
    """prompt a user to select a builtin category"""
    print('Please select a builtin category:')
    print(', '.join(BUILTINS_DATA))
    return input('> ')


def play_functions(list_of_functions):
    """given a list of functions, play the game"""
    right = wrong = 0
    while True:
        func = random.choice(list_of_functions)
        name = func.__name__
        print("Please tell me the name to which the following function's documentation belongs:")
        print(short_fn_doc(func))
        try:
            input_value = input('(Ctrl-C to quit) > ')
        except KeyboardInterrupt:
            print(f"Thanks for playing, you got {wrong} wrong, and {right} right.")
            break
        if input_value == name:
            right += 1
            print('correct!\n')
            print('*' * 80)
        else:
            wrong += 1
            print('No, the right answer is ' + name)
        time.sleep(1)

def play_types():
    "quiz the user on builtin types"
    print("Do you want to select the types themselves or their methods?")
    answer = input('> ')
    if answer == 'types':
        play_functions(BUILTINS_DATA['types'])
    elif answer == 'methods':
        play_methods()

def play_methods():
    "ask user for type to play methods"
    print("Which type's methods do you want to try?")
    answer_type = input('> ')
    dict_of_types = list_objs_to_dict(BUILTINS_DATA['types'])
    if answer_type in dict_of_types:
        play_functions(list_of_methods(dict_of_types[answer_type]))

def play_builtins():
    "quiz user on builtins"
    builtin_category = select_builtin_category()
    if builtin_category == 'types':
        play_types()
    elif builtin_category in BUILTINS_DATA:
        play_functions(BUILTINS_DATA[builtin_category])
    else:
        print('I did not understand that, please try again (Ctrl-C to exit)')
        play_builtins()

def play_game():
    "play the game!!"
    category = select_category()
    if category == 'builtins':
        play_builtins()
    #elif category == 'keywords':
    #    play_keywords()
    else:
        print('I did not understand that, please try again (Ctrl-C to exit)')
        play_game()

def main():
    "This is the entry point for the game"
    print('Welcome to Python Trainer, please select a category to train on.')
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print('Thanks for playing! Goodbye!')
        exit(0)

if __name__ == '__main__':
    main()
