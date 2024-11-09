"""
Student Loan Calculator

This program calculates the monthly payment, total payment, and total interest for student loans.
It reads loan parameters from an input file and writes the results to an output file.

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

#process loan

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

#read loan from input file
def read_loans_from_file(filename):
    """
    Read loan data from a file and return a list of loans
    """

    loans = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts= line.strip().split(',')
                if len(parts) != 3:
                    print(f"Invalid line format: {line}")
                    continue
                loan_amount, interest_rate, years = map(float, parts)
                loans.append((loan_amount, interest_rate, int(years)))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return loans


#ouput results to file
def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"Loan Amount: ${result['Loan Amount']}\n")
            file.write(f"Annual Interest Rate: {result['Annual Interest Rate']}%\n")
            file.write(f"Repayment Period: {result['Repayment Years']} years\n")
            file.write(f"Monthly Payment: ${result['Monthly Payment']}\n")
            file.write(f"Total Payment: ${result['Total Payment']}\n")
            file.write(f"Total Interest: ${result['total Interest']}\n")
            file.write("-" * 40 + "\n")

#main func
def main():
    input_file = 'loans_input.txt'
    output_file = 'loans_output.txt'
    loans = read_loans_from_file(input_file)

    if not loans:
        print("Invalid loan data. File missing.")
        return
    
    result = []
    for loan in loans:
        result = process_loan(loan)
        results.append(result)
    
    write_results_to_file(output_file, results)
    print(f"Loan calculations completed. Results written to {output_file}.")

#execute program
if __name__ == "__main__":
    main()



                                        

