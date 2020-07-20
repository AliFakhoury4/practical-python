# report.py
#
# Exercise 2.11

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



def create_report(portfolios, prices):
    rows = []
    for portfolio in portfolios:
        current_price = prices[portfolio[0]]
        change = current_price - portfolio[2]
        toAdd = (portfolio[0], portfolio[1], current_price, change)
        rows.append(toAdd)
    return rows
        

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


report = create_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
	print('%10s %10d %10.2f %10.2f' % row)