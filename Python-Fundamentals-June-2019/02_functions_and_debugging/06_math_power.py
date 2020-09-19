def to_the_power(number, power):
    """
    Raises the
    :param number:
    :param power:
    :return: result
    """
    return number ** power


if __name__ == '__main__':
    number = float(input())
    power = float(input())
    print(to_the_power(number, power))
