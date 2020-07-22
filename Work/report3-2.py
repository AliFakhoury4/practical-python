# report.py
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
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

def make_report_data(portfolios,prices):

    rows = []
    for portofolio in portfolios:
        current_price = prices[portofolio['name']]
        change = current_price - portofolio['price']
        summary = (portofolio['name'], portofolio['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile,pricefile):        
    portfolios = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolios,prices)

    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')