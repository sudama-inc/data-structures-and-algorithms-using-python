"""
Create own datatype.
Fraction datatype
"""


class Fraction(object):

    # Parameterized Constructor
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # return str(self.numerator) + "/" + str(self.denominator)
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __floordiv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __mod__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __pow__(self, other):
        return Fraction(self.numerator ** other, self.denominator ** other)


fr1 = Fraction(3, 4)
fr2 = Fraction(2, 3)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1 // fr2)
print(fr1 % fr2)
print(fr1 ** fr2)