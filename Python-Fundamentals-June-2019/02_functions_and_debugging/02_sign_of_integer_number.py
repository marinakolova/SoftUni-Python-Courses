def print_sign(n):
    """
    Prints the sign of the input number
    :param n: the input integer
    :return: None
    """
    if n < 0:
        print(f'The number {n} is negative.')
    elif n > 0:
        print(f'The number {n} is positive.')
    else:
        print(f'The number {n} is zero.')


if __name__ == '__main__':
    n = int(input())
    print_sign(n)