import math
from itertools import combinations


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_closest_points(points):
    closest_distance = float('+inf')
    result_points = []
    for comb in combinations(points, 2):
        x1, y1 = comb[0]
        x2, y2 = comb[1]
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        a = abs(p1.x - p2.x)
        b = abs(p1.y - p2.y)
        dist = math.sqrt(a * a + b * b)
        if dist < closest_distance:
            closest_distance = dist
            result_points = [comb[0], comb[1]]
    return closest_distance, result_points


if __name__ == '__main__':
    n = int(input())
    points = []

    for _ in range(n):
        points.append([int(number) for number in input().split()])

    distance, closes_points = find_closest_points(points)
    print(f'{distance:.3f}')
    for point in closes_points:
        print(f'({point[0]}, {point[1]})')
