# Question Link: https://www.desiqna.in/800/all-coding-questions-and-answers-asked-xplore-exam-25th-2021
class Blood:
    def __init__(self,*args):
        self.bloodGroup = args[0]
        self.unitInHand = args[1]

class BloodBank:
    def __init__(self,*args):
        self.bloodList = args[0]
    
    def isBloodAvailable(bGroup,unit):
        flag = False
        for obj in self.bloodList:
            if obj.bloodGroup == bGroup.upper():
                if obj.unitInHand > unit:
                    flag = True
                else:
                    flag = False
            else:
                flag = False

            
        return flag

    def findMinBloodStock():
        minBloodUnit = self.bloodList[0].unitInHand
        minBloodGroup = self.bloodList[0].bloodGroup
        for obj in self.bloodList:
            if obj.unitInHand < minBloodGroup:
                minBloodUnit = obj.unitInHand
                minBloodGroup = obj.bloodGroup
            minBloodList = []

            for obj2 in self.bloodList:
                if obj2.unitInHand == minBloodUnit:
                    minBloodList.append(obj2.bloodGroup)
        
        return minBloodList

if __name__ == "__main__":
    bloodList = []
    n = int(input())

    for i in range(n):
        bloodGroup = input()
        unitInHand = int(input())
        B = Blood(bloodGroup,unitInHand)
        bloodList.append(B)
    
    bGroup = input()
    unitReq = int(input())
    Bank = BloodBank(bloodList)
    res = Bank.isBloodAvailable(bGroup,unitReq)

    if(res):
        print("Blood Available.")
    else:
        print("Blood not Available.")

    minBlood = Bank.findMinBloodStock()

    for blood in minBlood:
        print(blood)
