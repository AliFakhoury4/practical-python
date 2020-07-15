# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
	f = open(filename)

	rows = csv.reader(f)
	headers = next(rows)

	total = 0

	for line in f:
	    row = line.split(',')
	    row[-1] = row[-1].strip()
	    total = total + float(row[1])*float(row[2])

	return total


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)