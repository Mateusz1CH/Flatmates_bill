from flat import Bill, Flatmate
from report import PdfReport

bill_amount = float(input("Buenos dias, enter the bill amount: "))
bill_period = input("What is the bill period? E.g December 2022 ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount = bill_amount, period = bill_period)
first_person = Flatmate(name = name1, days_in_house = days_in_house1)
second_person = Flatmate(name = name2, days_in_house = days_in_house2)

print(f"{first_person.name}", first_person.pays(bill=the_bill, flatmate2 = second_person))
print(f"{second_person.name}", second_person.pays(bill=the_bill, flatmate2 = first_person))

pdf_report = PdfReport(filename =f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=first_person, flatmate2=second_person, bill=the_bill)