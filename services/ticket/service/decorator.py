from flask import request
import json
from functools import wraps
from flask_restx import  marshal


def check_none(data):
    print(data)
    for k in data:
        if data[k] is None:
            return True
        if type(data[k]) is dict:
            return check_none(data[k])
    return False


def model_integrity(model):
    def real_integrity_check(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                data = marshal(json.loads(request.data), model)
                if check_none(data):
                    raise
            except:
                return {}, 400
            return f(*args, **kwargs)
        return wrapper
    return real_integrity_check


