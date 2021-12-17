# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 6
class Item:
    def __init__(self,*args):
        self.item_id = args[0]
        self.item_name = args[1]
        self.item_price = args[2]
        self.quantity_available = args[3]
    
    def calc_price(self,qty):
        if qty >= self.quantity_available:
            return qty*self.item_price
        else:
            return 0

class Store:
    def __init__(self,*args):
        self.item_list = args[0]
    
    def generate_bill(self,itemDict):
        s = 0
        for a,b in itemDict.items():
            for obj in item_list:
                if obj.item_name == a:
                    res = obj.calc_price(b)
                    s += res
        
        return s

if __name__ == "__main__":
    n = int(input())
    l = []

    for i in range(n):
        iId = int(input())
        iName = input()
        iPrice = int(input())
        iQty = int(input())

        I = Item(iId,iName,iPrice,iQty)
        l.append(I)
    
    S = Store(l)

    d = {}
    n1 = int(input())
    for j in range(n1):
        itemName = input()
        itemQty = int(input())
        d[itemName] = itemQty
    
    res = S.generate_bill(d)
    print(res)