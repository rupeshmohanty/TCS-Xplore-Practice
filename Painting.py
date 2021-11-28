# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-1/
class Painting:
	def __init__(self,*args):
		self.paintingId = args[0]
		self.paintingName = args[1]
		self.paintingPrice = args[2]
		self.paintingType = args[3]
	
class ShowRoom:
	def __init__(self,*args):
		self.paintingList = args[0]
	
	def getTotalPaintingPrice(self,pType):
		count = 0
		tprice = 0

		for obj in paintingList:
			if obj.paintingType.lower() == pType.lower():
				tprice += obj.paintingPrice
				count += 1
		
		if count == 0:
			return None
		else:
			return tprice
	
	def getPainterWithMaxCountOfPaintings(self):
		cDict = dict()

		for obj in paintingList:
			if obj.paintingName in cDict:
				cDict[obj.paintingName] += 1
			else:
				cDict[obj.paintingName] = 1
		
		# sort dictionary on the basis of the values!
		sort = dict(sorted(cDict.items(),key= lambda x : x[1]))

		maxArray = list(sort.values())
		m = maxArray[0]

		res = ""

		for k in list(sort.keys()):
			if res == "":
				if cDict[k] == m:
					res = k
			else:
				if cDict[k] == m:
					if cDict[k] < res:
						res = cDict[k]
		
		return res


if __name__ == "__main__":
	n = int(input())
	paintingList = []

	for i in range(n):
		paintingId = int(input())
		paintingName = input()
		paintingPrice = input()
		paintingType = input()

		P = Painting(paintingId,paintingName,paintingPrice,paintingType)
		paintingList.append(P)
	
	pType = input()
	S = ShowRoom(paintingList)

	totalPrice = S.getTotalPaintingPrice(pType)
	name = S.getPainterWithMaxCountOfPaintings()

	print(f'Total price: {totalPrice}')
	print(f'Painter with most paintings: {name}')