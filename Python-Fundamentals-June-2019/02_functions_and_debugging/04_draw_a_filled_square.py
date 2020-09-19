def print_outer_row(n):
    """
    Prints the outer row of the square
    :param n:
    :return: None
    """
    print('-' * 2 * n)


def print_middle_row(n):
    """
    Prints a middle row of the square
    :param n:
    :return:
    """
    inner_row_elements = '\/' * (n - 1)
    print(f'-{inner_row_elements}-')


def draw_filled_square(n):
    """
    Draws a filled square
    :return: None
    """
    print_outer_row(n)
    for i in range(n - 2):
        print_middle_row(n)
    print_outer_row(n)


if __name__ == '__main__':
    n = int(input())
    draw_filled_square(n)