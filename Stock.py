# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 2
class Stock:
    def __init__(self,*args):
        self.stockName = args[0]
        self.stockSector = args[1]
        self.stockValue = args[2]

class StockDemo:
    def __init__(self,*args):
        self.sList = args[0]
    
    def getStockList(self,sector):
        k = []
        for obj in self.sList:
            if obj.stockSector.lower() == sector.lower():
                if obj.stockValue > 500:
                    k.append(obj.stockName)
        return k

if __name__ == "__main__":
    stockList = []
    n = int(input())

    for i in range(n):
        stockName = input()
        stockSector = input()
        stockValue = int(input())
        S = Stock(stockName,stockSector,stockValue)
        stockList.append(S)
    
    D = StockDemo(stockList)
    sector = input()
    res = D.getStockList(sector)

    for stock in res:
        print(stock)