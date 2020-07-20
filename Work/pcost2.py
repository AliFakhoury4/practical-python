# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
	f = open(filename)

	rows = csv.reader(f)
	headers = next(rows)

	total_cost = 0

	for rowno, row in enumerate(rows, start=1):
		record = dict(zip(headers, row))
		try:
			shares = int(record['shares'])
			price = float(record['price'])
			total_cost += shares * price
		# This catches errors in int() and float() conversions above
		except ValueError:
			print(f'Row {rowno}: Bad row: {row}')

	return total_cost


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)