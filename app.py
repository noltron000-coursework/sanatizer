import re

def sanitize_input(input_text):
	'''
	cleans any string, of any length,
	containing any unicode character.
	'''
	return re.sub(r'[^a-zA-Z0-9\s]', '', input_text)
