# Exercise 7.6.8b

def reverse_list(original_list):
    '''
    Reverse the position of the given values in the list.
    original_list: (list) the list to be reversed
    output: (list) original_list backwards
    '''
    lenght = len(original_list)
    limit = lenght // 2
    for i in range (0, limit):
        aux = original_list[i]
        original_list[i] = original_list[lenght - i - 1]
        original_list[lenght - i - 1] = aux
    return original_list

print(reverse_list(['Di', 'buen', 'día', 'a', 'papa', 'jeje']))

# Exercise 7.6.9

def wrap(my_list):
    '''
    Count how many consecutive times a number appears
    my_list = (list) list of given values
    Output = (list) collection of tuples of values and theirs repetition
    '''
    previous = None
    result = []
    counter = None
    for number in my_list:
        if previous == number:
            counter += 1
        else:
            my_tuple = (previous, counter)
            counter = 1
            if previous != None:
                result.append(my_tuple)
        previous = number
    my_tuple = (previous, counter)
    result.append(my_tuple)
    return result
print(wrap([1, 1, 1, 3, 5, 1, 1, 3, 3]))

# Exercise 7.6.11

def cut_text(my_text, size):
    '''Divides the given text into pieces, avoid cutting words.

    my_text (str): Given text
    size (int): Size of each part of the solution
    output (list): Collection of pieces the original text is divided into
    '''
    result = []
    left = 0
    right = size
    total_length = len(my_text)
    while left < right:
        # The following snippet adjusts the right index in case it is
        # originally between two words
        if right < total_length:    # not required when right end is reached
            while left < right and my_text[right-1] != ' ' and my_text[right] != ' ':
                right -= 1

        # When both indexes match, this means it is not possible to get a piece
        # of requested size
        if left == right:
            print('No solution')
            return None

        piece = my_text[left:right]
        result.append(piece)
        left = right
        right = min(left + size, total_length)  # to consider last segment
    return result

example = 'This is a very nice text with a few words and whatever, blah, blah, blah...'
pieces = cut_text(example, 10)
print(pieces)