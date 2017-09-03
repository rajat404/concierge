# Third Party Imports
import waffle
from decorator import decorator as deco


def waffle_check(switch_name):
    @deco
    def wrapper(fn, *args, **kwargs):
        if not waffle.switch_is_active(switch_name):
            return 'waffle-disabled'
        return fn(*args, **kwargs)
    return wrapper
