from sys import argv

LOWERCASE_FIRST = 'a'
LOWECASE_LAST = 'z'
UPPERCASE_FIRST = 'A'
UPPERCASE_LAST = 'Z'
ADDITION_VALUE = 13
MODULE_VALUE = 26

def is_letter(anychar):
    '''
    Check if a given char is a letter or not.
    anychar: (str) any character.
    Output: (bool) True if it anychar is a letter or False if anychar is not a letter.
    '''
    is_lower_letter = anychar >= LOWERCASE_FIRST and anychar <= LOWECASE_LAST
    is_upper_letter = anychar >= UPPERCASE_FIRST and anychar <= UPPERCASE_LAST
    
    return is_lower_letter or is_upper_letter


def encode_char(char):
    '''
    Transform the given character in another.
    char: (str) any character.
    Output: (str) the given character encoded.
    '''
    value = (ord(char) + ADDITION_VALUE) % MODULE_VALUE
    encoded_char = chr(value)
    return encoded_char

def encode_line(anyline):
    '''
    Transform the given line in another
    anyline: (str) any line
    Output: (str) any line encoded
    '''
    encoded_line = ''
    for char in anyline:
        encoded_line += encode_char(char)
    return encoded_line

def rot13(textfile, destinyfile):
    '''
    Encodes a given file through an algorithm and saves the result into another file.
    textfile: (str) the original file to be encoded.
    destinyfile: (str) the file in which it is saved the information codified.
    '''
    with open(textfile) as originalfile, open(destinyfile, 'w') as newfile:
        for line in originalfile:
           
            newline = encode_line(line)
            newfile.write(newline)

rot13(argv[1], argv[2])
