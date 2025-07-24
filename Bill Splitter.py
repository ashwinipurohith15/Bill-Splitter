#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

#     def pays(self, bill, flatmate2):
#         weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
#         to_pay = bill.amount * weight
#         return to_pay


# In[6]:


import webbrowser
import os
from fpdf import FPDF

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts,
    and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)  # Ensure you have an icon at the specified path or adjust accordingly

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Calculate total days for all flatmates
        total_days = sum(flatmate.days_in_house for flatmate in flatmates)

        # Insert name and due amount for each flatmate
        pdf.set_font(family="Times", size=12)
        for flatmate in flatmates:
            share = (flatmate.days_in_house / total_days) * bill.amount
            pdf.cell(w=100, h=25, txt=flatmate.name, border=0)
            pdf.cell(w=150, h=25, txt=f"{share:.2f}", border=0, ln=1)

        # Optionally, change directory to 'files' or another specific path where you want to save your PDF reports
        # os.chdir("path/to/directory")
        pdf.output(self.filename)

        # Open the PDF automatically after generating it
        webbrowser.open('file://' + os.path.realpath(self.filename))


# In[ ]:


# Collect bill information
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

# Collect flatmates information
flatmates = []
num_flatmates = int(input("How many flatmates are there? "))

for i in range(num_flatmates):
    name = input(f"What is the name of flatmate {i+1}? ")
    days_in_house = int(input(f"How many days did {name} stay in the house during the bill period? "))
    flatmates.append(Flatmate(name, days_in_house))

the_bill = Bill(amount, period)

# Calculate total days to determine each flatmate's share
total_days = sum([flatmate.days_in_house for flatmate in flatmates])

# Calculate and print each flatmate's share
for flatmate in flatmates:
    share = (flatmate.days_in_house / total_days) * the_bill.amount
    print(f"{flatmate.name} pays: {share:.2f}")

# Generate PDF report
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmates, the_bill)  # Note: You'll need to adjust the generate method to handle multiple flatmates.


# In[ ]:




