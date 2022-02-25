# Question Link: https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Q8
class Bill:
    def __init__(self,*args):
        self.mobile = args[0]
        self.bill = args[1]
    
class Mobile:
    def __init__(self,*args):
        self.service_provider = args[0]
        self.mobile = args[1]
        self.data = args[2]
        self.payment = args[3]
    
    def calculateBill(self,l):
        m = []
        for obj in l:
            b = 0
            if obj.service_provider == "airtel":
                if obj.payment == "paytm":
                    b += 0.9*obj.data*11
                else:
                    b += obj.data*11
            else:
                b += obj.data*10
            m.append(Bill(obj.mobile,round(b)))
    
        return m

if __name__ == "__main__":
    n = int(input())
    mobileList = []

    for i in range(n):
        service_provider = input()
        mobile = int(input())
        data = int(input())
        payment_method = input()
        M = Mobile(service_provider,mobile,data,payment_method)
        mobileList.append(M)
    
    res = M.calculateBill(mobileList)

    for obj in res:
        print((obj.mobile,obj.bill))
