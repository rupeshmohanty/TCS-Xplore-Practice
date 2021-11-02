# Question Link: https://www.desiqna.in/865/tcs-xplore-cpa-exam-11th-march-2021-python-coding-solutions
class Player:
	def __init__(self,*args):
		self.playerName = args[0]
		self.playedCountry = args[1]
		self.playerAge = args[2]
		self.countryFrom = args[3]

def countPlayers(playerList,cname):
	count = 0
	for obj in playerList:
		if obj.countryFrom.lower() == cname.lower():
			count += 1

	return count

def getPlayerPlayedForMaxCountry(playerList):
	m = 0
	name = ""
	for obj in playerList:
		if len(obj.playedCountry) > m:
			m = len(obj.playedCountry)
			name = obj.playerName

	return name

if __name__ == "__main__":
	noOfPlayers = int(input())
	playerList = []
	for j in range(noOfPlayers):
		name = input()
		noOfCountries = int(input())
		countriesPlayed = []

		for i in range(noOfCountries):
			country = input()

			countriesPlayed.append(country)

		playerAge = int(input())
		countryFrom = input()

		P = Player(name,countriesPlayed,playerAge,countryFrom)
		playerList.append(P)

	countryName = input()
	c = countPlayers(playerList,countryName)
	n = getPlayerPlayedForMaxCountry(playerList)

	print(c)
	print(n)