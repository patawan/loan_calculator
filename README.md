# loan_calculator
Calculates the payment amount per period for a loan with given inputs
There are many times at work where I need to quickly calculate a monthly loan payment based on a few inputs (think of your financial calculator or the Excel PMT function). So I figured I could put one together quickly in python.


The calculator is based on this formula:
[ (rate / 100 / paymentsPerYr) * loanAmount ] /
(1 - [(1 + rate / 100) ** (-1 * (loanTerm * paymentsPerYr))])

https://en.wikipedia.org/wiki/Mortgage_calculator


The calculator takes a few inputs in the console:

    Loan Amount
    Loan Amortization
    Rate (in APR)
    Number of payments per year


After receiving the information it will spit out a monthly (or annually/quarterly/daily depending on input) payment.
