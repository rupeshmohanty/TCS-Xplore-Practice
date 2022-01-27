# Question Link: https://www.desiqna.in/918/all-previous-coding-questions-xplore-2021-study-resources
import math

class Person:
    def __init__(self,*args):
        self.name = args[0]
        self.height = args[1]
        self.weight = args[2]
        self.bmi = 0
        self.bmi_status = ""

    def calculateBmi(self):
        self.bmi = math.floor(self.weight/(self.height*self.height)) 

class Society:
    def __init__(self,*args):
        self.bmi_status = args[0]
        self.personList = args[1]
    
    def calculateBmiAndStatusByName(self,pname):
        for obj in self.personList:
            if obj.name.lower() == pname.lower():
                obj.calculateBmi()
                for obj1 in self.personList.keys():
                    if obj.bmi >= self.personList[obj1][0] and obj.bmi < self.personList[obj1][1]:
                        obj.bmi_status = self.personList[obj1]
                        return True
        
        return False

    def removeInvalidPerson(self,bmi_value):
        removed = []

        for obj in self.personList:
            if obj.bmi < bmi_value:
                removed.append(obj)

        if len(removed) > 0:
            return removed
        else:
            return None

if __name__ == "__main__":
    personList = []
    n = int(input())

    for i in range(n):
        name = input()
        height = int(input())
        weight = int(input())
        P = Person(name,height,weight)
        personList.append(P)

    n1 = int(input())
    statusDict = dict()
    for j in range(j):
        bmi_status = input()
        lower = int(input())
        upper = int(input())

        t = []
        t.append(lower)
        t.append(upper)

        t_tuple = tuple(t)

        statusDict[bmi_status] = t_tuple
    
    S = Society(statusDict,personList)
    personName = input()
    bmi = int(input())

    res = S.calculateBmiAndStatusByName(personName)
    if res:
        for obj in personList:
            if obj.name.lower() == personName.lower():
                if obj.bmi != 0:
                    print(obj.bmi)
                    print(obj.bmi_status)
    else:
        print("No Person Exists")

    fin = S.removeInvalidPerson(bmi)

    for obj1 in fin:
        print(obj1.name)
        print(obj1.bmi_status)   