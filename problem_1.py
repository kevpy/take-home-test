import string


def str_transform(text):
    ''' This function transforms a string and replaces each character of
        the alphabet with its value from a python dictionary

    A lookup table (python dict) is created which maps each value of the
    alphabet(key) to the reverse of the alphabet(value)

    Args:
        text: The function expects a string of text as a parameter

    Returns:
        Returns a transformed string that has its initial characters of
        the alphabet replaced with its value from a dictionary

    '''
    trans_table = dict(
        zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))

    new_str = []
    for i in list(text.lower()):
        if i in trans_table.keys():
            new_str.append(trans_table[i])
        else:
            new_str.append(i)
    return ''.join(new_str)


S = 'abcdefghijklmnopqrstuvwxyz'
print(str_transform(S))
