def getMorse(a):
	
	a = a.lower()	

	morseCode = ""

	morseCodeDictionary = {
		'1': '. - - - - /', '2': '. . - - - /', '3': '. . . - - /',
		'4': '. . . . - /', '5': '. . . . . /', '6': '- . . . . /',
		'7': '- - . . . /', '8': '- - - . . /','9' : '- - - - . /',
		'0': '- - - - - /',

		'a': '. - /', 'b': '- . . . /', 'c': '- . - . /', 'd': '- . . /',
		'e': '. /', 'f': '. . - . /', 'g': '- - . /', 'h': '. . . . /',
		'i': '. . /', 'j': '. - - - /', 'k': '- . - /', 'l': '. - . . /',
		'm': '- - /', 'n': '- . /', 'o': '- - - /', 'p': '. - - . /',
		'q': '- - . - /', 'r': '. - . /', 's': '. . . /', 't': '- /',
		'u': '. . - /', 'v': '. . . - /', 'w': '. - - /', 'x': '- . . - /',
		'y': '- . - - /', 'z': '- - . . /',
	}

	ignore = "`~!@#$%^&*()_+-=\\][|}{\';\":/.,?>< "

	for letter in a:
		if letter in ignore:
			morseCode += " "
		else:
			morseCode += str(morseCodeDictionary[letter])
	return morseCode

userInput = input("Enter message: ")
print(getMorse(userInput))
