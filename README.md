## Bill-Splitter Using Python

 A simple yet effective Python application designed to streamline the process of splitting bills among multiple people and generating a clean PDF report of the shared expenses. Perfect for roommates, group trips, or any shared financial arrangement!

# Features

- Easy Bill Input: Quickly enter bill amount, period, and individual flatmate details (name, amount paid).

- Fair Share Calculation: Automatically calculates each person's fair share of the bill.

- Owes/Gets Logic: Determines who owes money to whom and how much, simplifying settlements.

- PDF Report Generation: Creates a professional and printable PDF report summarizing the bill details and individual contributions using fpdf.

- User-Friendly Interface: (Mention if you have a GUI, CLI, or web interface. For your current code, it seems to be CLI-based, so you might say "Interactive Command-Line Interface.")

# How It Works

1. The BillSplitter application takes the total bill amount, the bill period (e.g., "July 2025"), and details for each participant (their name and the amount they've already paid). It then performs the following calculations:

2. Total Paid: Sums up the amounts paid by all participants.

3. Amount to Pay per Person: Divides the total bill by the number of participants.

4. Balance Calculation: For each person, it calculates the difference between their fair share and the amount they've already paid, indicating if they owe money or are owed money.

5. PDF Generation: Uses the fpdf library to compile all this information into a neatly formatted PDF document, including names, amounts paid, fair shares, and the final "owes/gets" breakdown.

 
