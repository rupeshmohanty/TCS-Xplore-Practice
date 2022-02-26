# Question link: https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Q10

class ParkedVehicle:
    def __init__(self,*args):
        self.vehicleSeq = args[0]
        self.fourWheeler = args[1]
        self.parkedFor = args[2]
        self.valetParking = args[3]
        self.parkedStatus = "Parked"

class ParkingLot:
    def __init__(self,*args):
        self.parkd_vehicles = args[0]

    def updateParkedStatus(self,lot_num):
        for obj in self.parkd_vehicles.keys():
            if obj == lot_num:
                self.parkd_vehicles[obj].parkedStatus = "Cleared"
                return (lot_num,self.parkd_vehicles[obj].parkedStatus)
        
        return None
    
    def getParkingCharges(self,lot_num):
        charge = 0
        for obj in self.parkd_vehicles.keys():
            if obj == lot_num:
                if self.parkd_vehicles[obj].fourWheeler == "Yes":
                    charge += self.parkd_vehicles[obj].parkedFor*50
                    if self.parkd_vehicles[obj].valetParking == "Yes":
                        charge += 10 
                else:
                    charge += self.parkd_vehicles[obj].parkedFor*30
                
        if charge == 0:
            return None
        else:
            return charge

if __name__ == "__main__":
    n = int(input())
    vehicleDict = {}

    for i in range(n):
        vehicleSeq = int(input())
        fourWheeler = input()
        parkedFor = float(input())
        valetParking = input()
        lNum = int(input())
        P = ParkedVehicle(vehicleSeq,fourWheeler,parkedFor,valetParking)
        vehicleDict[lNum] = P
    
    lot_num = int(input())
    L = ParkingLot(vehicleDict)
    res = L.updateParkedStatus(lot_num)
    total = L.getParkingCharges(lot_num)

    if res:
        print(res[0],res[1])
    else:
        print("Lot Number Invalid")
    
    if total:
        print(total)
    else:
        print("Lot Number Invalid")
