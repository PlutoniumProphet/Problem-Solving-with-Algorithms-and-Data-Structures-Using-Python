"""A fraction class."""


def gcd(m, n):
        """implements Euclid's Algorithm for greatest common divisor."""
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        """Overrides default add method that fails to add objects together."""
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        """Overiding equals to ensure deep equality (value not reference)
        is achieved."""
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x+y)
print(x == y)
