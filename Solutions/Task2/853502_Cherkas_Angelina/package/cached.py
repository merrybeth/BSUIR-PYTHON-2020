import functools


def cached(func):
    dict = {}

    @functools.wraps(func)
    def func_count(*args, **kwargs):
        key = args
        if key not in dict:
            dict[key] = func(*args, **kwargs)
        return dict[key]

    return func_count

@cached
def count(x):
    return x+1

@cached
def mul(x):
    return x*x
