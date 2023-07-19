from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def long(self):
        return 2 * pi * self.r

    def area(self):
        return pi * pow(self.r, 2)


class Rectangle:
    def __init__(self, a: int, b: int = None):
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    circle = Circle(11)
    print(f'{circle.long() = :.3f} {circle.area() = :.3f}')
    print(f'{circle.long() :.3f} {circle.area() :.3f}\n')

    rect = Rectangle(5)
    rect1 = Rectangle(5, 10)
    print(f'{rect.perimeter()= } {rect.area()= }')
    print(f'{rect1.perimeter()= } {rect1.area()= }')