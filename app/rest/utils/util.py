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

if __name__ == '__main__':
	get_key()