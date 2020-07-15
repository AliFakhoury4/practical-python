# report.py
#
# Exercise 2.4

def read_portfolio(filename):
	f = open(filename)

	headers = next(f).split(',')

	portfolio = []

	for line in f:
		row = line.split(',')
		row[-1] = row[-1].strip()
		holding = (row[0], int(row[1]), float(row[2]))
		portfolio.append(holding)

	return portfolio
	
print(read_portfolio('Data/portfolio.csv'))