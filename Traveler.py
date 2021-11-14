# Question Link: https://www.desiqna.in/746/what-was-the-python-coding-question-asked-cpa-tcs-xplore-15th
class Traveler:
	def __init__(self,*args):
		self.travelerName = args[0]
		self.traveledCountry = args[1]
		self.travelerAge = args[2]
		self.countryFrom = args[3]

class TravelAgency:
	def __init__(self,*args):
		travelerList = args[0]

	def countTravelersTraveledCountry(self,country):
		tcount = 0

		for obj in travelerList:
			for j in obj.traveledCountry:
				if j.lower() == country.lower():
					tcount += 1

		return tcount

	def getTravelerTraveledCountry(self):
		maxTravel = 0
		traveler = ""

		for obj in travelerList:
			if len(obj.traveledCountry) >= maxTravel:
				traveler = obj.travelerName

		return traveler


if __name__ == "__main__":
	travelerList = []
	noOfTravelers = int(input())

	for i in range(noOfTravelers):
		travelerName = input()
		traveledCountry = input()
		travelerAge = int(input())
		countryFrom = input()

		T = Traveler(travelerName,traveledCountry,travelerAge,countryFrom)

		travelerList.append(T)

	TA = TravelAgency(travelerList)
	country = input()

	count = TA.countTravelersTraveledCountry(country)
	maxTraveler = TA.getTravelerTraveledCountry()

	print(count)
	print(maxTraveler)


