def compare(comparison_type, first_value, second_value):
    """
    Compares the passed value, depending on the type
    :param comparison_type:
    :param first_value:
    :param second_value:
    :return:
    """
    if comparison_type == 'int':
        return compare_integers(first_value, second_value)
    elif comparison_type == 'char':
        return compare_chars(first_value, second_value)
    else:
        return compare_strings(first_value, second_value)


def compare_integers(first, second):
    """
    Returns the greater of the two integers
    :param first:
    :param second:
    :return: int
    """
    return max(int(first), int(second))


def compare_chars(first, second):
    """
    Returns the greater of the two characters
    :param first:
    :param second:
    :return: char
    """
    return chr(max(ord(first), ord(second)))


def compare_strings(first, second):
    """
    Returns the greater of the two strings
    :param first:
    :param second:
    :return: string
    """
    return first if first > second else second


if __name__ == '__main__':
    comparison_type = input()
    first_value = input()
    second_value = input()
    print(compare(comparison_type, first_value, second_value))
