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
		price = 0
		count = 0

		for obj in dairyList:
			if obj.dairyBrand.lower() == dBrand.lower() and obj.productType.lower() == pType:
				updatedPrice = price + price*weightageDict[obj.grade]/100
				count += 1
		
		if count == 0:
			return None
		else:
			return updatedPrice

if __name__ == "__main__":
	noOfDairy = int(input())
	dairyList = []
	wDict = dict()

	for i in range(noOfDairy):
		dairyId = int(input())
		dairyBrand = input()
		productType = input()
		price = int(input())
		grade = input()

		D = DairyProduct(dairyId,dairyBrand,productType,price,grade)
		dairyList.append(D)

	# count for dictionary elements!
	n1 = int(input())

	for j in range(n1):
		g = input()
		w = int(input())
		
		wDict[g] = w
	
	P = ProductGrade(dairyList,wDict)
	dBrand = input()
	pType = input()

	res = P.priceBasedOnBrandAndType(dBrand, pType)
	if res != None:
		print(f'Dairy Brand: {dBrand}')
		print(f'Price: {res}')
	else:
		print("No dairy product found")
