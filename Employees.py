# Question Link: https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 5
class Employee:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.role = args[2]
        self.salary = args[3]
    
    def increment_salary(self,inc):
        self.salary += (self.salary*inc)/100
    
class Organization:
    def __init__(self,*args):
        self.org_name = args[0]
        self.emps = args[1]
    
    def calculate_salary(self,role,perc):
        inc_ppl_list = []

        for obj in self.emps:
            if obj.role.lower() == role.lower():
                obj.increment_salary(perc)
                inc_ppl_list.append((obj.name,obj.salary))

        if len(inc_ppl_list) > 0:
            return inc_ppl_list
        else:
            return None
    
if __name__ == "__main__":
    n = int(input())
    empList = []

    for i in range(n):
        eid = int(input())
        name = input()
        role = input()
        salary = int(input())

        empList.append(Employee(eid,name,role,salary))
    
    O = Organization(empList)
    eRole = input()
    perc = int(input())
    res = O.calculate_salary(eRole, perc)

    for i in res:
        print(res[0])
        print(res[1])
