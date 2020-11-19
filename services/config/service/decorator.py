from flask import request
import json
from functools import wraps
from flask_restx import  marshal

def model_integrity(model):
    def real_integrity_check(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                data = marshal(json.loads(request.data), model)
                if next((False for k in data if bool(data[k])),True):
                    raise
            except:
                return {}, 400
            return f(*args, **kwargs)
        return wrapper
    return real_integrity_check


