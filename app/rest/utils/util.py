from flask import jsonify

import random
import string
import time 

# this method create genarates random alpha numeric key
def get_key():
	key = ''
	chars = string.lowercase  + string.digits + string.uppercase
	size = 8
	key = ''.join((random.choice(chars)) for x in range(size))
	current_time = str(int(round(time.time(),0)))
	key = key + current_time
	return key

def get_current_ts_in_ms():
	 return str(int(round(time.time() * 1000)))

#used for mysql tables.
def get_current_ts():
	return time.strftime('%Y-%m-%d %H:%M:%S')

def to_json(status_code, data):
	return jsonify({'status' : status_code, 'data': data }), status_code

if __name__ == '__main__':
	get_key()