import datetime
import re
import simplejson
import pandas as pd

# no JSON.stringigy in Python
SEP = "!!-_-____-_-!!"

class JS:
    def __init__(self, js_code: str):
        self.js_code = "%s%s%s" % (SEP, js_code, SEP)


def _json_dump_default(o: object):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, JS):
        return o.js_code
    if isinstance(o, pd.DataFrame):
        return o.to_dict(orient='records')
    return o

def json_dump_options(options: object):
    return simplejson.loads(simplejson.dumps(options, indent=2, default=_json_dump_default, ignore_nan=True))
