
# INF201 - Deliverable 4
# Task 2:  Fractions


from __future__ import annotations


class Fraction:
    """Represents a math fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Making the fraction

        Arguments:
                numerator (int): represents the numerator of the fraction.
                denominator (int): represents the denominator of the fraction.
        
        """
        self.denominator = denominator
        self.numerator = numerator
        if not isinstance(self.denominator, int):
            raise TypeError("denominator has to be an int")
        if not isinstance(self.numerator, int):
            raise TypeError("numerator has to be int")
        if denominator <= 0:
            raise ValueError("denominator cannot be below or equal 0")
        
    def __eq__(self, other: object) -> bool:
        """Return True if 2 fractions are equal."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __ne__(self, other: object) -> bool:
        """Returns true if two fractions are not equal."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator != self.denominator * other.numerator
    
    def __lt__(self, other: object) -> bool:
        """Returns true if a fraction is less then another."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator
    
    def __le__(self, other: object) -> bool:
        """Returns true if this fraction is less or equal to another."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= self.denominator * other.numerator
    
    def __gt__(self, other: object) -> bool:
        """Returns true if this fraction is bigger than another."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator
    
    def __ge__(self, other: object) -> bool:
        """Returns true if a fracion is bigger or equal to another."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= self.denominator * other.numerator
    
    def __add__(self, other: Fraction ) -> Fraction:
        """Returns sum of 2 fractions as one new fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self,other: Fraction) -> Fraction:
        """Returns the differance beetween 2 fractions as one new fraction"""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self,other: Fraction) -> Fraction:
        """Returns the product of 2 fractions as a new fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented
        total_numerator = self.numerator * other.numerator
        total_denominator = self.denominator * other.denominator
        return Fraction(total_numerator, total_denominator)
    
    def __float__(self) -> float:
        """Returns a floating-point value of this fraction"""
        return self.numerator / self.denominator
