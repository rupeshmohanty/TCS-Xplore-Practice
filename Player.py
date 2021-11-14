# Question Link: https://www.desiqna.in/865/tcs-xplore-cpa-exam-11th-march-2021-python-coding-solutions
class Player:
	def __init__(self,*args):
		self.playerName = args[0]
		self.playedCountry = args[1]
		self.playerAge = args[2]
		self.countryFrom = args[3]


def countPlayers(playerList,country):
	pcount = 0

	for obj in playerList:
		if obj.countryFrom.lower() == country.lower():
			pcount += 1

	return pcount

def getPlayerPlayedForMaxCountry(playerList):
	playerDict = {}

	for obj in playerList:
		if obj.playerName in playerDict:
			playerDict[obj.playerName] += 1
		else:
			playerDict[obj.playerName] = 1

	max_played = 0
	player_name = ""

	for i in list(playerDict.keys()):
		if playerDict[i] > max_played:
			player_name = i

	return player_name

if __name__ == "__main__":
	n = int(input())
	playerList = []

	for i in range(n):
		playerName = input()
		n1 = int(input())
		playedCountry = []

		for j in range(n1):
			countryName = input()
			playedCountry.append(countryName)

		playerAge = int(input())
		countryFrom = input()

		P = Player(playerName,playedCountry,playerAge,countryFrom)

		playerList.append(P)

	country = input()

	playerCount = countPlayers(playerList,country)
	player = getPlayerPlayedForMaxCountry(playerList)

	print(playerCount)
	print(player)