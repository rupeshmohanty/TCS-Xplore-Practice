# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-3/
class DairyProduct:
	def __init__(self,*args):
		self.dairyId = args[0]
		self.dairyBrand = args[1]
		self.productType = args[2]
		self.price = args[3]
		self.grade = args[4]

class ProductGrade:
	def __init__(self,*args):
		self.dairyList = args[0]
		self.weightageDict = args[1]

	def priceBasedOnBrandAndType(self,dBrand,pType):
		ans = []

		for obj in dairyList:
			if obj.dairyBrand.lower() == dBrand.lower() and obj.productType.lower() == pType.lower():
				weightage = weightageDict[obj.grade]
				obj.price += obj.price*weightage/100
				ans.append((dBrand,obj.price))

		if len(ans) > 0:
			return ans
		else:
			return None

if __name__ == "__main__":
	dairyList = []
	wDict = {}

	n = int(input())
	for i in range(n):
		dairyId = int(input())
		dairyBrand = input()
		productType = input()
		price = int(input())
		grade = input()

		D = DairyProduct(dairyId,dairyBrand,productType,price,grade)

		dairyList.append(D)

	dictLen = int(input())
	for i in range(dictLen):
		key = input()
		value = int(input())

		wDict[key] = value

	P = ProductGrade(dairyList,wDict)
	dBrand = input()
	pType = input()

	res = P.priceBasedOnBrandAndType(dBrand,pType)
	
	if res != None:
		print("Dairy Brand: " + res[0])
		print("Price: " + res[1])
	else:
		print('No dairy product found!')