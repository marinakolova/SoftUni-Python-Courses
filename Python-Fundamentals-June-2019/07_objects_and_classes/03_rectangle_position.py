class Rectangle:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def is_inside(self, rectangle):
        return self.left >= rectangle.left and self.right <= rectangle.right \
               and self.top <= rectangle.top and self.bottom <= rectangle.bottom


if __name__ == '__main__':
    left1, top1, width1, height1 = [int(n.strip()) for n in input().split()]
    left2, top2, width2, height2 = [int(n.strip()) for n in input().split()]
    r1 = Rectangle(left1, top1, width1, height1)
    r2 = Rectangle(left2, top2, width2, height2)
    result = r1.is_inside(r2)
    if result:
        print('Inside')
    else:
        print('Not inside')
