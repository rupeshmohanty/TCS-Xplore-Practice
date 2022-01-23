# Question Link: https://www.desiqna.in/865/tcs-xplore-cpa-exam-11th-march-2021-python-coding-solutions
class Player:
	def __init__(self,*args):
		self.playerName = args[0]
		self.playedCountry = args[1]
		self.playerAge = args[2]
		self.countryFrom = args[3]
	
def countPlayer(pList,cname):
	count = 0
	for obj in pList:
		if obj.countryFrom.lower() == cname.lower():
			count += 1
	
	return count

def getPlayerPlayedForMaxCountry(pList):
	m = 0
	name = ""

	for obj in pList:
		if len(obj.playedCountry) > m:
			m = len(obj.playedCountry)
			name = obj.playerName
	
	return name

if __name__ == "__main__":
	players = []
	n = int(input())
	for i in range(n):
		playerName = input()
		n1 = int(input())
		playedCountry = []
		for j in range(n1):
			cName = input()
			playedCountry.append(cName)
	
		playerAge = int(input())
		countryFrom = input()

		P = Player(playerName,playedCountry,playerAge,countryFrom)
		players.append(P)

	country = input()
	res = countPlayer(players, country)
	res1 = getPlayerPlayedForMaxCountry(players)
	print(res)
	print(res1)