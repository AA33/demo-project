__author__ = 'abhishekanurag'


def get_int_or_neg(num_string):
    try:
        num = int(num_string)
    except ValueError:
        num = -1
    return num