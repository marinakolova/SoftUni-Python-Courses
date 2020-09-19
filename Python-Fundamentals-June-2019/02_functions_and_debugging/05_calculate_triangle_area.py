def calc_triangle_area(base, height):
    """
    Calculates the area of the triangle
    :param base:
    :param height:
    :return: area
    """
    return (base * height) / 2


if __name__ == '__main__':
    base = float(input())
    height = float(input())
    area = calc_triangle_area(base, height)
    print(f'{area:.12g}')