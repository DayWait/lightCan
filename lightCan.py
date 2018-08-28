def getMorse(word):
    """
    Converts a word to morse code and returns the morse code. Ignores Non-Alphanumeric characters
    :param word: User input word
    :return: A word converted to morse code
    """

    # Dictionary/Key List to convert alphanumeric to morse code
    morseCodeDictionary = {
        # Digits
        '1': '. - - - - /', '2': '. . - - - /', '3': '. . . - - /',
        '4': '. . . . - /', '5': '. . . . . /', '6': '- . . . . /',
        '7': '- - . . . /', '8': '- - - . . /', '9': '- - - - . /',
        '0': '- - - - - /',

        # Alphabets
        'a': '. - /', 'b': '- . . . /', 'c': '- . - . /', 'd': '- . . /',
        'e': '. /', 'f': '. . - . /', 'g': '- - . /', 'h': '. . . . /',
        'i': '. . /', 'j': '. - - - /', 'k': '- . - /', 'l': '. - . . /',
        'm': '- - /', 'n': '- . /', 'o': '- - - /', 'p': '. - - . /',
        'q': '- - . - /', 'r': '. - . /', 's': '. . . /', 't': '- /',
        'u': '. . - /', 'v': '. . . - /', 'w': '. - - /', 'x': '- . . - /',
        'y': '- . - - /', 'z': '- - . . /',
    }

    word = word.lower()  # Convert user input into lowercase. There are no uppercase morse code
    morseCode = ""  # Holds the character converted to morse code

    # Converts only alphanumeric letters to morse code
    for letter in word:
        if letter.isalnum():
            morseCode += morseCodeDictionary[letter]

    return morseCode  # Returns the word that has been turned into morse code


# Test code
userInput = input("Enter message: ")
print(getMorse(userInput))
