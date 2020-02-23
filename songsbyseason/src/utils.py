import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"%...Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"%...{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug

#See https://realpython.com/primer-on-python-decorators/ 