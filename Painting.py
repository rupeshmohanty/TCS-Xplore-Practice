# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-1/
class Painting:
	def __init__(self,*args):
		self.paintingId = args[0]
		self.painterName = args[1]
		self.paintingPrice = int(args[2])
		self.paintingType = args[3]

class ShowRoom:
	def __init__(self,plist):
		self.paintingList = plist

	# Get total painting price!
	def getTotalPaintingPrice(self,pType):
		c = 0
		total_price = 0
		for obj in self.paintingList:
			if obj.paintingType.lower() == pType.lower():
				total_price += obj.paintingPrice
				c = 1

		if c:
			return total_price
		else:
			return None

	# To get painter with max count of paintings!
	def getPainterWithMaxCountOfPaintings(self):
		nameCount = {}

		for obj in self.paintingList:
			if obj.painterName not in nameCount:
				nameCount[obj.painterName] = 1
			else:
				nameCount[obj.painterName] += 1

		m = 0
		name = ""
		for i in list(nameCount.keys()):
			if nameCount[i] > m:
				m = nameCount[i]
				name = i

		return name

if __name__ == "__main__":
	paintingList = []
	noOfObj = int(input())

	for i in range(noOfObj):
		paintingId = input()
		painterName = input()
		paintingPrice = input()
		paintingType = input()

		P = Painting(paintingId,painterName,paintingPrice,paintingType)

		paintingList.append(P)

	S = ShowRoom(paintingList)

	pType = input()
	tot_price = S.getTotalPaintingPrice(pType)
	name = S.getPainterWithMaxCountOfPaintings()

	if tot_price != None:
		print(tot_price)
	else:
		print("Painting not found")

	print(name)
