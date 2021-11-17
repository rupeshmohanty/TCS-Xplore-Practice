# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-2/
class Property:
	def __init__(self,*args):
		self.property_type = args[0]
		self.property_value = args[1]
		self.max_bid_price = args[2]

class Tender:
	def __init__(self,*args):
		self.buyerName = args[0]
		self.propertyType = args[1]
		self.bidPrice = args[2]


def bidProperty(propertyList,tenderList):
	ans = []
	typeSet = set()
	removeObj = set()
	objDict = {}

	for obj in tenderList:
		for obj1 in propertyList:
			if obj.propertyType.lower() == obj1.property_type.lower():
				if obj.propertyType.lower() in objDict:
					if objDict[obj.propertyType][1] < obj.bidPrice:
						objDict[obj.propertyType.lower()] = (obj.buyerName, obj.bidPrice)

				if obj.bidPrice >= obj1.property_value and obj.bidPrice <= obj1.max_bid_price:
					typeSet.add(obj.propertyType.lower())
					removeObj.add(obj1)

	# add names to the list!
	for pType in typeSet:
		ans.append(objDict[pType][0])

	# removing the properties!
	for obj2 in removeObj:
		propertyList.remove(obj2)

	return ans

if __name__ == "__main__":
	propertyList = []
	tenderList = []

	# add properties!
	n1 = int(input())
	for i in range(n1):
		property_type = input()
		property_value = int(input())
		max_bid_price = int(input())

		P = Property(property_type,property_value,max_bid_price)

		propertyList.append(P)

	# add tenders!
	n2 = int(input())
	for j in range(n2):
		buyerName = input()
		productType = input()
		bidPrice = int(input())

		T = Tender(buyerName,propertyType,bidPrice)

		tenderList.append(T)

	res = bidProperty(propertyList,tenderList)
	
	if len(res) == 0:
		print("Property Not found")
	else:	
		for a in res:
			print(a)

	# property types!
	for b in propertyList:
		print(propertyList.property_type)
