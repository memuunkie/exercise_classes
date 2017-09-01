import random
from datetime import datetime

"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """A high-level abstract class for melon orders."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None

        if qty > 100:
            raise TooManyMelonserror()

    def get_base_price(self):
        """Calculate a random base price for melon"""
        base_price = random.randint(5, 9)

        if self.species == 'Christmas melon':
            base_price *= 1.5

        current_time = datetime.now()

        if current_time.weekday() in range(5):
            if current_time.hour in range(8,13):
                base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        return (1 + self.tax) * self.qty * self.get_base_price()

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class  TooManyMelonserror(ValueError):
    """Returns error if more than 100 melons are ordered."""

    def __init__(self):
    """Docstring!"""
        super(TooManyMelonserror, self).__init__("Too many melons!")


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)

        self.order_type = 'domestic'
        self.tax = 0.08

    def get_base_price(self):
        """Calculate a random base price for melon"""
        return super(DomesticMelonOrder, self).get_base_price()

    def get_total(self):
        """Calculate price, including tax."""
        return super(DomesticMelonOrder, self).get_total()

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super(DomesticMelonOrder, self).mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
#
        self.country_code = country_code
        self.order_type = 'international'
        self.tax = 0.17

    def get_base_price(self):
        """Calculate a random base price for melon"""
        return super(InternationalMelonOrder, self).get_base_price()

    def get_total(self):
        """Calculate price, including tax."""
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total = total + 3
            return total
        else:
            return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super(InternationalMelonOrder, self).mark_shipped()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the government."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty)

        self.tax = 0
        self.passed_inspection = False

    def get_base_price(self):
        """Calculate a random base price for melon"""
        return super(GovernmentMelonOrder, self).get_base_price()

    def get_total(self):
        """Calculate price, including tax."""
        return super(GovernmentMelonOrder, self).get_total()

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super(GovernmentMelonOrder, self).mark_shipped()

    def mark_inspected(self):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True

