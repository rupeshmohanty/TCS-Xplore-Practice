# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 1
class Payslip:
    def __init__(self,*args):
        self.basicSalary = args[0]
        self.hra = args[1]
        self.ita = args[2]

class PaySlipDemo:
    def __init__(self,*args):
        self.payslip = args[0]
    
    def getHighestPF(self):
        m = 0

        for obj in self.payslip:
            if 12*obj.basicSalary // 100 > m:
                m = 12*obj.basicSalary // 100
        
        return m

if __name__ == "__main__":
    payslip = []
    n = int(input())

    for i in range(n):
        basicSalary = int(input())
        hra = int(input())
        ita = int(input())

        P = Payslip(basicSalary,hra,ita)

        payslip.append(P)
    
    Pay = PaySlipDemo(payslip)
    res = Pay.getHighestPF()

    print(res)