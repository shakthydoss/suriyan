def register(data):
	error = None
	is_valid = True
	if not (data):
		error = "Invalid data"
		is_valid = False
	if not ('name' in data):
		error = "Invalid name"
		is_valid = False
	return is_valid, error

