# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 5
class Employee:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.role = args[2]
        self.salary = args[3]
    
    def increment_salary(self,perc):
        self.salary += self.salary*perc / 100
    

class Organization:
    def __init__(self,*args):
        self.org_name = args[0]
        self.employeeList = args[1]
    
    def calculate_salary(self,eRole,inc):
        result = []

        for obj in self.employeeList:
            if obj.role.lower() == eRole.lower():
                obj.increment_salary(inc)
                result.append(obj)
            
        return result
    
if __name__ == "__main__":
    n = int(input())
    employeeList = []

    for i in range(n):
        eId = int(input())
        name = input()
        role = input()
        salary = int(input())
    
        E = Employee(eId,name,role,salary)
        employeeList.append(E)
    
    O = Organization("TCS",employeeList)
    eRole = input()
    inc = int(input())

    res = O.calculate_salary(eRole, inc)

    for i in res:
        print(i.name)
        print(i.salary)
    