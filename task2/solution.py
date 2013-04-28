from collections import OrderedDict
from itertools import starmap


def groupby(func, seq):
    return {func(x):
            [item for item in seq if func(item) == func(x)]
            for x in seq}


def composition(function_1, function_2):
    return lambda x: function_1(function_2(x))


def iterate(func):
    result = lambda x: x

    while True:
        yield result
        result = composition(func, result)


def zip_with(func, *iterables):
    return starmap(func, zip(*iterables))


def cache(func, cache_size):
    cache_order = OrderedDict()

    def func_cashed(*args):
        if args in cache_order:
            return cache_order[args]
        result = func(*args)

        if cache_size:
            if len(cache_order) == cache_size:
                cache_order.popitem(last=False)
            cache_order[args] = result

        return result
    return func_cashed
