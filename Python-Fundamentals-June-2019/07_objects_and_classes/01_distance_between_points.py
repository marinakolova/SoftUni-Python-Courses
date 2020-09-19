import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p1, p2):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    distance = math.sqrt(a * a + b * b)
    return distance


if __name__ == '__main__':
    x1, y1 = [int(number) for number in input().split()]
    x2, y2 = [int(number) for number in input().split()]
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    result = calc_distance(p1, p2)
    print(f'{result:.3f}')
