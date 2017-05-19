# Problem 2


def chunk_string(string, length):
    """ This function splits a string of text to equal chunks of text/ string
    with equal length.

    Args:
        string: accepts a string of any length as a parameter.

        length: accepts a integer as a parameter.

    Returns:
        The function returns a python list with each value of the list having
        equal length
    """
    return [string[0+i:length+i] for i in range(0, len(string), length)]


S = 'Just a test string'
N = 3

print(chunk_string(S, N))
