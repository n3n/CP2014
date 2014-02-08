def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if first(word) != last(word):
		return False
	elif len(word) <= 2:
		return True
	else:
		return is_palindrome(middle(word))

text = raw_input("Press message: ")
print "Is palindrome?", is_palindrome(text)

