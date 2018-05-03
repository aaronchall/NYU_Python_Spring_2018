def export(fn):
    global __all__
    # add the function.__name__ to __all__
    try:
        __all__.append(fn.__name__)
    except NameError:
        __all__ = [fn.__name__]
    return fn


@export
def func1():
    _func()


def _func():
    pass


@export
def func2():
    pass


def do_not_intend_to_support():
    pass
