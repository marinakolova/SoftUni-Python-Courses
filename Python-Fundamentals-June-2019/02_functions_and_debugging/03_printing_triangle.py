def print_middle_line(n):
    """
    Prints the middle line of the triangle
    :param n: the input integer
    :return: None
    """
    print(' '.join([str(i + 1) for i in range(n)]))


def print_triangle_half(n, is_upper_half = True):
    """
    Prints the half of the triangle
    :param n: the input integer
    :param is_upper_half: whether it should print the upper half of the triangle or not
    :return:
    """
    for row in range(n - 1):
        rows = row + 1 if is_upper_half else n - row - 1
        for col in range(rows):
            print(col + 1, end=' ')
        print()


def print_triangle(n):
    """
    Prints a triangle
    :param n: the input integer
    :return: None
    """
    print_triangle_half(n)
    print_middle_line(n)
    print_triangle_half(n, False)


if __name__ == '__main__':
    n = int(input())
    print_triangle(n)