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

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)

        self.order_type = 'domestic'
        self.tax = 0.08

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

    def get_total(self):
        """Calculate price, including tax."""
        return super(InternationalMelonOrder, self).get_total()

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super(InternationalMelonOrder, self).mark_shipped()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
