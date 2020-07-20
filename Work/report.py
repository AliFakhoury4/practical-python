# report.py
#
# Exercise 2.7

def read_portfolio(filename):
	f = open(filename)

	headers = next(f).split(',')

	portfolio = []

	for line in f:
		row = line.split(',')
		row[-1] = row[-1].strip()
		row[0] = row[0].replace('"', '')
		holding = (row[0], int(row[1]), float(row[2]))
		portfolio.append(holding)

	return portfolio
	

def read_prices(filename):
	f = open(filename)


	prices = {}
	for line in f:
		if len(line) > 1:
			row = line.split(',')
			row[-1] = row[-1].strip()
			row[0] = row[0].replace('"', '')
			holding = {row[0]: float(row[1])}
			prices.update(holding)

	return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

total_cost = 0.0
for value in portfolio:
    total_cost += value[1]*value[2]

print('Total cost', total_cost)

total_value = 0.0
for value in portfolio:
    total_value += value[1]*prices[value[0]]

print('Current value', total_value)
print('Gain', total_value - total_cost)
