import calendar
import random
import string
import time
from datetime import datetime

from flask import jsonify


# this method create genarates random alpha numeric key
def get_key():
    key = ''
    chars = string.lowercase + string.digits + string.uppercase
    size = 8
    key = ''.join((random.choice(chars)) for x in range(size))
    current_time = str(int(round(time.time(), 0)))
    key = key + current_time
    return key


def get_unixtime():
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    return str(unixtime)


def to_json(status_code, data):
    return jsonify({'status': status_code, 'data': data}), status_code
