class Doctor:
    def __init__(self,*args):
        self.doctorId = args[0]
        self.doctorName = args[1]
        self.specialization = args[2]
        self.consulationFee = args[3]

class Hospital:
    def __init__(self,*args):
        doctorDB = args[0]
    
    def searchByDoctorName(self,dName):
        dList = []
        for obj in self.doctorDB.values():
            if obj.doctorName.lower() == dName.lower():
                dList.append(obj)
        
        if len(dList) > 0:
            return dList
        else:
            return None
    
    def calculateConsulationFeeBySpecialization(self,specialization):
        total = 0

        for obj in doctorDB.values():
            if obj.specialization.lower() == specialization.lower():
                total += obj.consulationFee
        
        if total != 0:
            return total
        else:
            return 0
    
if __name__ == "__main__":
    n = int(input())
    doctorDict = dict()

    for i in range(n):
        doctorId = int(input())
        doctorName = input()
        specialization = input()
        consulationFee = int(input())
        doctorDict[doctorId] = Doctor(doctorId,doctorName,specialization,consulationFee)
    
    H = Hospital(doctorDict)
    dName = input()
    s = input()

    doctorList = H.searchByDoctorName(dName)
    totalBill = H.calculateConsulationFeeBySpecialization(s)

    if doctorList:
        for obj in doctorList:
            print(obj.doctorId)
            print(obj.doctorName)
            print(obj.specialization)
            print(obj.consulationFee)
    else:
        print("No Doctor Exists with the given DoctorName")
    
    if totalBill == 0:
        print("No Doctor with the given specialization")
    else:
        print(totalBill)