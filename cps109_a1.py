"""
Student Loan Calculator

This program calculates the monthly payment, total payment, and total interest for student loans.
Users can input multiple loan entries via the terminal, and the results are written to an output file.

Functional Requirements:
- Input Parameters:
  - Loan Amount
  - Annual Interest Rate
  - Repayment Period (years)
- Outputs:
  - Monthly Payment
  - Total Payment
  - Total Interest
- Additional Features:
  - Handles multiple loan entries
  - Uses various Python constructs including loops, conditionals, functions, and file I/O
"""

import math

#monthly payment calculator
def calculate_monthly_payment(loan_amount, annual_interest_rate, repayment_years):
    monthly_interest_rate = annual_interest_rate/100/12
    number_of_payments = repayment_years * 12
    if monthly_interest_rate == 0:
        return loan_amount / number_of_payments
    #montly loan payment formula
    monthly_payment = loan_amount * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)) \
                      / (math.pow(1 + monthly_interest_rate, number_of_payments) - 1)
    return monthly_payment

#process a single loan
def process_loan(loan):
    loan_amount, annual_interest_rate, repayment_years = loan
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, repayment_years)
    total_payment = monthly_payment * repayment_years * 12
    total_interest = total_payment - loan_amount
    return {
        'Loan Amount': loan_amount,
        'Annual Interest Rate': annual_interest_rate,
        'Repayment Years': repayment_years,
        'Monthly Payment': round(monthly_payment, 2),
        'Total Payment': round(total_payment, 2),
        'Total Interest': round(total_interest, 2)
    }


#ouput results to file
def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for idx, result in enumerate(results, start=1):
            file.write(f"Loan Amount: ${result['Loan Amount']}\n")
            file.write(f"Annual Interest Rate: {result['Annual Interest Rate']}%\n")
            file.write(f"Repayment Period: {result['Repayment Years']} years\n")
            file.write(f"Monthly Payment: ${result['Monthly Payment']}\n")
            file.write(f"Total Payment: ${result['Total Payment']}\n")
            file.write(f"Total Interest: ${result['Total Interest']}\n")
            file.write("-" * 40 + "\n")
    print(f"\nLoan calculations completed. Results written to {filename}.")

#main func
def main():

    output_file = 'loans_output.txt'
    results = []

    print("Welcome to the Student Loan Calculator!\n")

    while True:
        print("Enter loan details:")

        # Input Loan Amount
        while True:
            try:
                loan_amount = float(input("  Loan Amount ($): "))
                if loan_amount < 0:
                    print("  Please enter a positive number for the loan amount.")
                    continue
                break
            except ValueError:
                print("  Invalid input. Please enter a numeric value for the loan amount.")

        # Input Annual Interest Rate
        while True:
            try:
                annual_interest_rate = float(input("  Annual Interest Rate (%): "))
                if annual_interest_rate < 0:
                    print("  Please enter a non-negative number for the interest rate.")
                    continue
                break
            except ValueError:
                print("  Invalid input. Please enter a numeric value for the interest rate.")

        # Input Repayment Period
        while True:
            try:
                repayment_years = int(input("  Repayment Period (years): "))
                if repayment_years <= 0:
                    print("  Please enter a positive integer for the repayment period.")
                    continue
                break
            except ValueError:
                print("  Invalid input. Please enter an integer value for the repayment period.")

        # Process the loan
        loan = (loan_amount, annual_interest_rate, repayment_years)
        result = process_loan(loan)
        results.append(result)
        print("  Loan processed successfully.")

        # Ask user if they want to add another loan
        while True:
            cont = input("Do you want to add another loan? (y/n): ").strip().lower()
            if cont in ['y', 'n']:
                break
            else:
                print("  Please enter 'y' for yes or 'n' for no.")

        if cont != 'y':
            break
        print("")  # Add an empty line for better readability

    # Write all results to the output file
    write_results_to_file(output_file, results)

#execute program
if __name__ == "__main__":
    main()
    