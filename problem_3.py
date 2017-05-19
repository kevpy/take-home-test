# Problem 3


def temp_example(timestamp, reading, threshold):
    """ This function outputs the timestamp when the threshold temperature
    is exceeded.

    Args:
        timestamp: accepts a list as a parameter

        reading: accepts a list as a parameter

    Returns:
        timestamp: yeilds the timestamp when the temperature was exceeded
    """
    for val in range(len(reading)):
        if reading[val] > threshold and reading[val-1] < threshold:

            # index of timestamp is the same as the index of the reading
            # when the threshold is exceeded
            yield timestamp[val]


T = [1460545900, 1460545910, 1460545920, 1460545930, 1460545940, 1460545950]
R = [0, 7, 12, 18, 8, 17]
Q = 10

exceeded_pionts = list(temp_example(T, R, Q))
print(exceeded_pionts)
