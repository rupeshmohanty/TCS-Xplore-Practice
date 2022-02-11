# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 3
class Public:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.gender = args[2]
        self.distance = args[3]
    
class Bill:
    def __init__(self,*args):
        self.pList = args[0]
    
    def calculateDiscount(self,pId,perc):
        d = []
        for obj in self.pList:
            if obj.id == pId:
                d.append((perc*obj.distance)/100)

        return d

if __name__ == "__main__":
    passengerList = []
    n = int(input())

    for i in range(n):
        pId = int(input())
        name = input()
        gender = input()
        distance = int(input())
        P = Public(pId,name,gender,distance)
        passengerList.append(P)
    
    B = Bill(passengerList)
    passengerId = int(input())
    perc = int(input())
    res = B.calculateDiscount(passengerId,perc)

    for j in res:
        print(f'Discount of 101 is: {j}')