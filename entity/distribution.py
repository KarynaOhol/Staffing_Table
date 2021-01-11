class Distribution:

    def __init__(self, division, staff_unit):
        self.division = division
        self.staff_unit = staff_unit

    def __str__(self):
        return """
    DISTRIBUTION [
    """ + self.division.__str__() + "\n" + self.staff_unit.__str__() + "\n\t]"
