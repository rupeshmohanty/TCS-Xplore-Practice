# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 2
class Stock:
    def __init__(self,*args):
        self.StockName = args[0]
        self.StockSector = args[1]
        self.StockValue = args[2]

class StockDemo:
    def __init__(self):
        pass
    
    def getStockList(self,stockList,StockSector):
        finList = []

        for obj in stockList:
            if obj.StockSector.lower() == StockSector.lower() and obj.StockValue > 500:
                finList.append(obj)
        
        return finList

if __name__ == "__main__":
    stockList = []
    n = int(input())

    for i in range(n):
        StockName = input()
        StockSector = input()
        StockValue = int(input())

        S = Stock(StockName,StockSector,StockValue)
        stockList.append(S)
    
    Sd = StockDemo()
    sector = input()

    res = Sd.getStockList(stockList, sector)
    
    for k in res:
        print(k.StockName)