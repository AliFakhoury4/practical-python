import fileparse314 as fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

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
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')