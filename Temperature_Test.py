# INF201 - Deliverable 4
# Task 1: Temperature tests

import pytest
from Temperature import Temperature


def test_initialization():
    """Test default and lowercase units."""

    assert Temperature(25).unit == "C"
    assert Temperature(25, "f").unit == "F"

    # Check read-only attributes.
    with pytest.raises(AttributeError):
        Temperature(25).value = 30


def test_invalid_values():
    """Test invalid units and temperatures."""

    with pytest.raises(ValueError):
        Temperature(25, "X")

    for value, unit in [(-274, "C"), (-460, "F"), (-1, "K")]:
        with pytest.raises(ValueError):
            Temperature(value, unit)


def test_conversions():
    """Test known reference temperatures."""

    # Celsius, Fahrenheit, Kelvin
    values = [
        (-273.15, -459.67, 0),
        (-40, -40, 233.15),
        (0, 32, 273.15),
        (37, 98.6, 310.15),
        (100, 212, 373.15),
    ]

    for c, f, k in values:
        assert Temperature(c, "C").to_fahrenheit() == pytest.approx(f)
        assert Temperature(f, "F").to_celsius() == pytest.approx(c)
        assert Temperature(k, "K").to_celsius() == pytest.approx(c)


def test_round_trip():
    """Test conversion back to the original unit."""

    temp = Temperature(25, "C")
    result = temp.convert_to("F").convert_to("K").convert_to("C")

    assert temp == result


def test_comparisons():
    """Test comparisons between different units."""

    a = Temperature(0, "C")
    b = Temperature(32, "F")
    c = Temperature(100, "C")

    assert a == b
    assert a != c
    assert a < c
    assert a <= b
    assert c > a
    assert c >= a


def test_formatting():
    """Test the string representations."""

    temp = Temperature(25, "C")

    assert str(temp) == "25.00 °C"
    assert repr(temp) == "Temperature(25.0, 'C')"