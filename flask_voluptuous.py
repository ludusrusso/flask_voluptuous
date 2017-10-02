from flask import request, abort
import functools
from voluptuous import *

__version__ = '0.1.1'

_ADMITTED_LOCATIONS = ['json', 'form', 'args']

def expect(schema, location='json'):
    def decorator(f):
        if location not in _ADMITTED_LOCATIONS:
            raise AttributeError('{} location not admitted'.format(location))
        @functools.wraps(f)
        def wrapper(*args, **kargs):
            if location in ['args', 'form']:
                req = getattr(request, location).to_dict()
            else:
                req = getattr(request, location)
            try:
                request_locs = schema(req)
            except Invalid as e:
                abort(406, str(e))
            kargs[location] = request_locs
            return f(*args, **kargs)
        return wrapper
    return decorator
