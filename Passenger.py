# Question Link: https://themotivatingindian.in/tcs-xplore-opa-python-2nd-march-solution/
# Q1
class Passenger:
	def __init__(self,*args):
		self.passengerName = args[0]
		self.passengerAge = args[1]
		self.distanceTravelled = args[2]
	
def calculateTicketFare(passengerList,farePerKM):
	totalTicketFare = 0

	for obj in passengerList:
		price = 0
		price = obj.distanceTravelled*farePerKM

		if obj.passengerAge >= 60 or obj.passengerAge < 12:
			tax = 0
		elif obj.passengerAge >= 21 or obj.passengerAge <= 59:
			tax = 0.12*price
		elif obj.passengerAge >= 12 or obj.passengerAge <= 20:
			tax = 0.1*price
		
		price+=tax
		tprice+=price
	
	return tprice

def Countseniorjunior(passengerList):
	count=0
	for obj in passengerList:
		if obj.passengerAge >= 60 or obj.passengerAge < 12:
			count += 1
		
	return count

if __name__ == "__main__":
	n = int(input())
	pList = []

	for i in range(n):
		passengerName = input()
		passengerAge = int(input())
		distanceTravelled = int(input())

		P = Passenger(passengerName,passengerAge,distanceTravelled)
		pList.append(P)
	
	rate = int(input())

	totalPrice = calculateTicketFare(pList, rate)
	count = Countseniorjunior(pList)

	print(f'Total fare of all passengers: {totalPrice}')
	print(f'Total count of junior and senior passengers: {count}')