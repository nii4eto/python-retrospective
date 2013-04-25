from collections import deque


def groupby(func, seq):
    return {func(x):
            [item for item in seq if func(item) == func(x)]
            for x in seq}


def composition(func_1, func_2):
    return lambda x: func_1(func_2(x))


def iterate(func):
    result = lambda x: x

    while True:
        yield result
        result = composition(func, result)


def zip_with(func, *iterables):
    i = zip(*iterables)

    while True:
        yield func(*next(i))


def cache(func, cache_size):
    values = {}
    cache_order = deque()

    def func_cashed(*args):
        if args in values:
            return values[args]

        result = func(*args)

        if cache_size:
            if len(values) == cache_size:
                values.pop(cache_order.popleft())
            cache_order.append(args)
            values[args] = result

        return result
    return func_cashed
