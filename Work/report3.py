# report.py
#
#exercise 2.16

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

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
        current_price = prices[portfolio['name']]
        change = current_price - portfolio['price']
        toAdd = (portfolio['name'], portfolio['shares'], current_price, change)
        rows.append(toAdd)
    return rows
        

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')


report = create_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)