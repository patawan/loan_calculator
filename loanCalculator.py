# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:15:24 2019

@author: phess
"""

loanAmount = int(input('What is the loan amount? '))
rate = int(input('What is the rate (APR)? '))
paymentsPerYr = int(input('How many payments will there be each year? '))
loanTerm = int(input('What is the loan term? (in years) '))

def paymentCalc(loanAmount, rate, paymentsPerYr, loanTerm):
    numerator = (rate / 100 / paymentsPerYr) * loanAmount
    denominator = (1 + rate / 100) ** (-1 * (loanTerm * paymentsPerYr))
    return str(round((numerator / (1 - denominator)),2))
    
print('The payment each period is $' + paymentCalc(loanAmount, rate, paymentsPerYr, loanTerm))
