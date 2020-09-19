import math


class Box:

    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.width = int(Point.calc_distance(self.upper_left, self.upper_right))
        self.height = int(Point.calc_distance(self.upper_left, self.bottom_left))

    def calc_perimeter(self):
        return int(2 * self.height + 2 * self.width)

    def calc_area(self):
        return int(self.height * self.width)

    def __str__(self):
        return f'Box: {self.width}, {self.height}\n' \
            f'Perimeter: {self.calc_perimeter()}\n' \
            f'Area: {self.calc_area()}'


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calc_distance(p1, p2):
        a = abs(p1.x - p2.x)
        b = abs(p1.y - p2.y)
        distance = math.sqrt(a * a + b * b)
        return distance


if __name__ == '__main__':
    boxes = []

    while True:
        inp = input()
        if inp == 'end':
            for box in boxes:
                print(box)
            break

        inp = inp.split(' | ')
        upper_left_x, upper_left_y = [int(x) for x in inp[0].split(':')]
        upper_right_x, upper_right_y = [int(x) for x in inp[1].split(':')]
        bottom_left_x, bottom_left_y = [int(x) for x in inp[2].split(':')]
        bottom_right_x, bottom_right_y = [int(x) for x in inp[3].split(':')]
        upper_left_point = Point(upper_left_x, upper_left_y)
        upper_right_point = Point(upper_right_x, upper_right_y)
        bottom_left_point = Point(bottom_left_x, bottom_left_y)
        bottom_right_point = Point(bottom_right_x, bottom_right_y)
        boxes.append(Box(upper_left_point, upper_right_point, bottom_left_point, bottom_right_point))
