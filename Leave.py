# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 4

class Leave:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.leaves = args[2]
    
class Company:
    def __init__(self,*args):
        self.emps = args[0]
    
    def display_leave(self,empId,Ltype):
        for obj in self.emps:
            if obj.id == empId:
                return obj.leaves[Ltype]
    
    def number_of_leaves(self,empId,Ltype,req):
        for obj in self.emps:
            if obj.id == empId:
                if obj.leaves[Ltype] >= req:
                    return "GRANTED"
                else:
                    return "REJECTED"

if __name__ == "__main__":
    n = int(input())
    empList = []
    leaves = {}

    for i in range(n):
        empId = int(input())
        name = input()
        leaves["EL"] = int(input())
        leaves["SL"] = int(input())
        leaves["CL"] = int(input())

        L = Leave(empId,name,leaves)
        empList.append(L)
    
    C = Company(empList)
    eid = int(input())
    Ltype = input()
    req = int(input())
    nol = C.display_leave(eid, Ltype)  
    res = C.number_of_leaves(eid, Ltype, req)

    print(nol)
    print(res)