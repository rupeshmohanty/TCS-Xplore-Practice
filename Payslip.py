# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 1
class Payslip:
    def __init__(self,*args):
        self.bs = args[0]
        self.hra = args[1]
        self.ita = args[2]
    
class PaySlipDemo:
    def __init__(self):
        self.m = 0
    
    def highestPF(self,l):
        k = []
        for obj in l:
            pf = 0.12*obj.bs
            k.append(pf)
        
        return int(max(k))

if __name__ == "__main__":
    payList = []
    n = int(input())

    for i in range(n):
        bs = int(input())
        hra = int(input())
        ita = int(input())
        P = Payslip(bs,hra,ita)
        payList.append(P)

    D = PaySlipDemo()
    res = D.highestPF(payList)
    print(res)