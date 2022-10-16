class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Create a Pdf file that contain data about the flatmates such as their name, their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount = 6000, period = "August 2022")
Antonio = Flatmate(name = 'Antonio', days_in_house = 20)
Antonina = Flatmate(name = 'Antonina', days_in_house = '29')

print(Antonina.pays(bill=the_bill))