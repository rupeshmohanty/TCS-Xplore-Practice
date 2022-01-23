# Question Link: https://www.desiqna.in/746/what-was-the-python-coding-question-asked-cpa-tcs-xplore-15th
class Traveler:
	def __init__(self,*args):
		self.travelerName = args[0]
		self.traveledCountry = args[1]
		self.travelerAge = args[2]
		self.countryFrom = args[3]

class TravelAgency:
	def __init__(self,*args):
		self.travelerList = args[0]
	
	def countTravelersTraveledCountry(cname):
		count = 0

		for obj in self.travelerList:
			if cname in obj.traveledCountry:
				count += 1
		
		return count
	
	def getTravelerTravelledMaxCountry():
		m = 0
		name = []

		for obj in self.travelerList:
			if len(obj.traveledCountry) > m:
				m = len(obj.traveledCountry)
				name.append(obj.travelerName) 
		
		return name[len(name)-1]

if __name__ == "__main__":
	travelerList = []
	n = int(input())

	for i in range(n):
		travelerName = input()
		n1 = int(input())
		traveledCountry = []
		for j in range(n1):
			cTraveled = input()
			traveledCountry.append(cTraveled)
		
		travelerAge = int(input())
		countryFrom = input()

		T = Traveler(travelerName,traveledCountry,travelerAge,countryFrom)
		travelerList.append(T)
	
	cname = input()
	A = TravelAgency(travelerList)
	c = A.countTravelersTraveledCountry(cname)
	res = A.getTravelerTravelledMaxCountry()

	print(c)
	print(res) 