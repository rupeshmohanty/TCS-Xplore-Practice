# Question Link: https://themotivatingindian.in/tcs-xplore-opa-python-2nd-march-solution/
# Q1
class Passenger:
	def __init__(self,*args):
		self.id = args[0]
		self.name = args[1]
		self.gender = args[2]
		self.distance = args[3]

class Bill:
	def __init__(self,pList):
		self.pList = pList

	def calDiscount(self,pid,discPerc):
		discount = 0
		for obj in self.pList:
			if obj.id == pid:
				discount = discPerc*obj.distance/100
				break

		return discount

if __name__ == "__main__":
	noOfPassengers = int(input())
	passengerList = []

	for i in range(noOfPassengers):
		pid = input()
		name = input()
		gender = input()
		distance = int(input())

		P = Passenger(pid,name,gender,distance)

		passengerList.append(P)

	B = Bill(passengerList)

	passId = input()
	perc = int(input())

	discount = B.calDiscount(passId,perc)

	print(f'discount of { passId } is: { discount }')