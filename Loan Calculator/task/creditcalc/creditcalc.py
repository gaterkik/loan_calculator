import argparse
import math
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment')
    parser.add_argument('--principal')
    parser.add_argument('--periods')
    parser.add_argument('--interest')
    return parser


def number_payments(loan_interest, monthly_payment, loan_principal):
    temp = monthly_payment / (monthly_payment - (loan_principal * loan_interest / 1200))
    number_pay = math.ceil(math.log(temp, ((loan_interest / 1200) + 1)))
    years = int(number_pay // 12)
    months = math.ceil(number_pay - (years * 12))
    if months == 0:
        print('It will take {} years to repay this loan!'.format(years))
    else:
        print('It will take {} years and {} months to repay this loan!'.format(years, months))
    overpayment = (monthly_payment * number_pay) - loan_principal
    print('Overpayment = {}'.format(overpayment))


def monthly_payments(loan_principal, number_payment, loan_interest):
    i = loan_interest / 1200
    monthly_pay = math.ceil((loan_principal * i * (1 + i) ** number_payment) / ((1 + i) ** number_payment - 1))
    print('Your annuity payment = {}!'.format(monthly_pay))
    overpayment = (monthly_pay * number_payment) - loan_principal
    print('Overpayment = {}'.format(overpayment))


def principal_calc(number_payment, loan_interest, payment):
    i = loan_interest / 1200
    temp = (i * (1 + i) ** number_payment) / ((1 + i) ** number_payment - 1)
    principal = math.floor(payment / temp)
    overpayment = (payment * number_payment) - principal
    print('Your loan principal = {}!'.format(principal))
    print('Overpayment = {}'.format(overpayment))


def diff_payments_calc(principal, periods, interest):
    i = interest / 1200
    summ = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        summ += payment
        print('Month {}: payment is {}'.format(m, payment))

    overpayment = summ - principal
    print('Overpayment = {}'.format(overpayment))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if len(sys.argv) == 5 and namespace.interest is not None:
        if namespace.type == 'annuity':
            if namespace.payment is None:
                monthly_payments(int(namespace.principal), int(namespace.periods), float(namespace.interest))
            if namespace.principal is None:
                principal_calc(int(namespace.periods), float(namespace.interest), int(namespace.payment))
            if namespace.periods is None:
                number_payments(float(namespace.interest), int(namespace.payment), int(namespace.principal))
        elif namespace.type == 'diff':
            diff_payments_calc(int(namespace.principal), int(namespace.periods), float(namespace.interest))
    else:
        print('Incorrect parameters.')