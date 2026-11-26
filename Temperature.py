# INF201 - Deliverable 4
# Task 1: Temperatures

from functools import total_ordering


@total_ordering
class Temperature:
    """Represent a temperature in Celsius, Fahrenheit or Kelvin."""

    def __init__(self, value, unit="C"):
        """Create a temperature and check its value and unit."""

        unit = unit.upper() if isinstance(unit, str) else ""

        if unit not in ("C", "F", "K"):
            raise ValueError("Invalid unit")

        # Check absolute zero.
        minimum = {"C": -273.15, "F": -459.67, "K": 0}

        if value < minimum[unit]:
            raise ValueError("Below absolute zero")

        self._value = float(value)
        self._unit = unit

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_kelvin(self):
        """Convert to Kelvin."""

        if self.unit == "C":
            return self.value + 273.15
        if self.unit == "F":
            return (self.value + 459.67) * 5 / 9
        return self.value

    def to_celsius(self):
        """Convert to Celsius."""

        if self.unit == "C":
            return self.value
        return self.to_kelvin() - 273.15

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""

        if self.unit == "F":
            return self.value
        return self.to_kelvin() * 9 / 5 - 459.67

    def convert_to(self, unit):
        """Return a new converted temperature."""

        if not isinstance(unit, str):
            raise ValueError("Invalid unit")

        unit = unit.upper()

        if unit == "C":
            return Temperature(self.to_celsius(), unit)
        if unit == "F":
            return Temperature(self.to_fahrenheit(), unit)
        if unit == "K":
            return Temperature(self.to_kelvin(), unit)

        raise ValueError("Invalid unit")

    def __str__(self):
        """Display the temperature with two decimals."""

        symbol = self.unit

        # Add a degree symbol unless the unit is Kelvin.
        if self.unit != "K":
          symbol = "°" + self.unit

        return f"{self.value:.2f} {symbol}"


    def __repr__(self):
        """Show how the temperature object was created."""

        return f"Temperature({self.value}, '{self.unit}')"


    def __eq__(self, other):
        """Check if two temperatures are equal."""

        if not isinstance(other, Temperature):
            return NotImplemented

        difference = abs(self.to_kelvin() - other.to_kelvin())

        return difference <= 1e-9

    def __lt__(self, other):
        """Check if one temperature is lower than another."""

        if not isinstance(other, Temperature):
           return NotImplemented

        difference = other.to_kelvin() - self.to_kelvin()

        return difference > 1e-9
    