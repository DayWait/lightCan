def getMorse(a):

	# function called getMorse that converts a string into a string of morse code
  seperated by forward slashes.
  
  # make a lower case
	a = a.lower()	

	# declare new empty string, "morse"
	morse = ""

	# numbers
	one = str(". - - - - /")
	two = str(". . - - - /")
	three = str(". . . - - /")
	four = str(". . . . - /")
	five = str(". . . . . /")
	six = str("- . . . . /") 
	seven = str("- - . . . /")
	eight = str("- - - . . /") 
	nine = str("- - - - . /")
	zero = str("- - - - - /")

	# letter
	aa = str(". - /")
	bb = str("- . . . /")
	cc = str("- . - . /")
	dd = str("- . . /")
	ee = str(". /")
	ff = str(". . - . /")
	gg = str("- - . /")
	hh = str(". . . . /")
	ii = str(". . /")
	jj = str(". - - - /")
	kk = str("- . - /")
	ll = str(". - . . /")
	mm = str("- - /")
	nn = str("- . /")
	oo = str("- - - /")
	pp = str(". - - . /")
	qq = str("- - . - /")
	rr = str(". - . /")
	ss = str(". . . /")
	tt = str("- /")
	uu = str(". . - /")
	vv = str(". . . - /")
	ww = str(". - - /")
	xx = str("- . . - /")
	yy = str("- . - - /")
	zz = str("- - . . /")


	# ignore
	ignore = " ~`!@#$%^&*()_+|}{\\][\'\";:/.,?><"
		
	for letter in a:
		if letter == "a":
			morse += aa
		if letter == "b":
			morse += bb
		if letter == "c":
			morse += cc
		if letter == "d":
			morse += dd
		if letter == "e":
			morse += ee
		if letter == "f":
			morse += ff
		if letter == "g":
			morse += gg
		if letter == "h":
			morse += hh
		if letter == "i":
			morse += ii
		if letter == "j":
			morse += jj
		if letter == "k":
			morse += kk
		if letter == "l":
			morse += ll
		if letter == "m":
			morse += mm
		if letter == "n":
			morse += nn
		if letter == "o":
			morse += oo
		if letter == "p":
			morse += pp
		if letter == "q":
			morse += qq
		if letter == "r":
			morse += rr
		if letter == "s":
			morse += ss
		if letter == "t":
			morse += tt
		if letter == "u":
			morse += uu
		if letter == "v":
			morse += vv
		if letter == "w":
			morse += ww
		if letter == "x":
			morse += xx
		if letter == "y":
			morse += yy
		if letter == "z":
			morse += zz
		if letter == "1":
			morse += one
		if letter == "2":
			morse += two
		if letter == "3":
			morse += three
		if letter == "4":
			morse += four
		if letter == "5":
			morse += five
		if letter == "6":
			morse += six
		if letter == "7":
			morse += seven
		if letter == "8":
			morse += eight
		if letter == "9":
			morse += nine
		if letter == "0":
			morse += zero
		if letter in ignore:
			morse += ""
	return morse

userInput = input("Enter message: ")

print(getMorse(userInput))
