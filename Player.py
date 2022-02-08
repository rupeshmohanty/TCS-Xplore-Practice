# Question Link: https://www.desiqna.in/865/tcs-xplore-cpa-exam-11th-march-2021-python-coding-solutions
class Player:
	def __init__(self,*args):
		self.playerName = args[0]
		self.playedCountry = args[1]
		self.playerAge = args[2]
		self.countryFrom = args[3]
	
def countPlayers(pList,cName):
	cnt = 0

	for obj in pList:
		if obj.countryFrom.lower() == cName.lower():
			cnt += 1
	
	return cnt

def getPlayerPlayedForMaxCountry(pList):
	m = 0
	name = ""

	for obj in pList:
		if len(obj.playedCountry) > m:
			m = len(obj.playedCountry)
			name = obj.playerName
	
	return name

if __name__ == "__main__":
	n = int(input())
	playerList = []

	for i in range(n):
		playerName = input()
		n1 = int(input())
		cList = []
		for j in range(n1):
			country = input()
			cList.append(country)
		playerAge = int(input())
		countryFrom = input()
		P = Player(playerName,cList,playerAge,countryFrom)
	
	cName = input()
	c = countPlayers(playerList, cName)
	res = getPlayerPlayedForMaxCountry(playerList)

	print(c)
	print(res)