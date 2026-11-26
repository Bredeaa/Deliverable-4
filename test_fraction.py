# INF201 - Deliverable 4
# Task 2:  Tests for fractions


import pytest
from fraction import Fraction


def test_int_values() -> None:
    """Testing valid int numerator and denominator"""
    values = Fraction(3,4)
    values2 = Fraction(-3,4)
    assert values.numerator == 3
    assert values.denominator == 4
    assert values2.numerator == -3

def test_invalid_types() -> None:
    """Testing a non-int value triggers TypeError with raise"""
    with pytest.raises(TypeError):
        Fraction(3.2, 2)
    with pytest.raises(TypeError):
        Fraction(2, 3.2)
    with pytest.raises(TypeError):
        Fraction(3.2, 3.2)

def test_invalid_denominator() -> None:
    """Testing that 0 or negative values for denominator raises ValueError"""
    with pytest.raises(ValueError):
        Fraction(1, 0)
    with pytest.raises(ValueError):
        Fraction(1, -1)

def test_invalid_fractions() -> None:
    """Testing comparison beetween a Fraction with a non-fraction raises TypeError"""
    with pytest.raises(TypeError):
        Fraction(3, 4) < 0.5

def test_eq() -> None:
    """Testing equality beetween two  equal fractions"""
    values = Fraction(1,2)
    values2 = Fraction(2,4)
    assert values == values2

def test_ne() -> None:
    """Testing not equality beetwwen two fractions that are not equal"""
    values = Fraction(1,2)
    values2 = Fraction(3,4)
    assert values != values2

def test_lt() -> None:
    """Testing less-than comparison for positive and negative fracitons"""
    values = Fraction(1,2)
    values2 = Fraction(3,4)
    values3 = Fraction(-1,2)
    values4 = Fraction(-1,4)
    assert values < values2
    assert values3 < values4

def test_le() -> None:
    """Testing less-than or equal comparison for smaller and equal fractions"""
    values = Fraction(1,2)
    values2 = Fraction(3,4)
    values3 = Fraction(6,8)
    assert values <= values2
    assert values2 <= values3

def test_gt() -> None:
    """Testing greater-than comparison beetween fractions"""
    values = Fraction(2,2)
    values2 = Fraction(3,4)
    assert values > values2

def test_ge() -> None:
    """Testing greater-than and equal comparisons for greater and equal fractions"""
    values = Fraction(2,2)
    values2 = Fraction(3,4)
    values3 = Fraction(6,8)
    assert values >= values2
    assert values2 >= values3 

def test_add() -> None:
    """Testing fraction addition and TypeError for Fractions and non-fractions"""
    values = Fraction(3,4)
    values2 = Fraction(-1,2)
    number = 5
    assert values + values2 == Fraction(1,4) 
    with pytest.raises(TypeError):
        values + number

def test_sub() -> None:
    """Testing fraction subtracion and TypeError for fractions and non-fractions"""
    values = Fraction(3,4)
    values2 = Fraction(-1,2)
    number = 5
    assert values - values2 == Fraction(5,4)
    with pytest.raises(TypeError):
        values - number

def test_mul() -> None:
    """Testing fraction multiplication and TypeError for fractions and non-fractions"""
    values = Fraction(3,4)
    values2 = Fraction(-1,2)
    number = 5
    assert values * values2 == Fraction(-3,8)
    with pytest.raises(TypeError):
        values * number

def test_float() -> None:
    """Test converting exact and repeating fractions to float"""
    assert float(Fraction(-1,2)) == pytest.approx(-0.5)
    assert float(Fraction(1,3)) == pytest.approx(1/3)







    


