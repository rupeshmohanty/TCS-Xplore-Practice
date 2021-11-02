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

	def countTravelersTraveledCountry(self,countryName):
		count = 0
		for obj in self.travelerList:
			if obj.traveledCountry.lower() == countryName.lower():
				count += 1

		return count

	def getTravelerTravelledMaxCountry(self):
		m = 0
		ans = []
		for obj in self.travelerList	:
			if len(obj.traveledCountry) >= m:
				m = len(obj.traveledCountry)
				ans.append(obj.travelerName)

		return ans[len(ans)-1]

if __name__ == "__main__":
	travelerList = []
	noOfTravelers = int(input())

	for i in range(noOfTravelers):
		travelerName = input()
		countOfCountries = int(input())
		traveledCountry = []

		for j in range(countOfCountries):
			countryName = input()

			traveledCountry.append(countryName)
		
		travelerAge = int(input())
		countryFrom = input()

		T = Traveler(travelerName,traveledCountry,travelerAge,countryFrom)
		travelerList.append(T)

	TA = TravelAgency(travelerList)
	cname = input()
	c = TA.countTravelersTraveledCountry(cname)
	m = TA.getTravelerTravelledMaxCountry()

	print(c)
	print(m)
