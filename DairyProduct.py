# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-3/
class DairyProduct:
	def __init__(self,dairyId,dairyBrand,productType,price,grade):
		self.dId = dairyId
		self.dBrand = dairyBrand
		self.pType = productType
		self.price = price
		self.grade = grade

class ProductGrade:
	def __init__(self,dairyList,weightageDict):
		self.dList = dairyList
		self.wDict = weightageDict

	def priceBasedOnBrandAndType(self,dairyBrand,productType):
		ans = []
		for obj in self.dList:
			if obj.dBrand.lower() == dairyBrand.lower() and obj.pType.lower() == productType.lower():
				updatedPrice = obj.price + obj.price*self.wDict[obj.grade]/100
				ans.append((brand,obj.price))

		if(len(ans)):
			return ans
		else:
			return None

if __name__ == "__main__":
	n = int(input())
	dairyProducts = []
	for i in range(n):
		dairyId = int(input())
		dairyBrand = input()
		productType = input()
		price = int(input())
		grade = input().lower()
		
		dp = DairyProduct(dairyId,dairyBrand,productType,price,grade)

		dairyProducts.append(dp)

	n1 = int(input())

	weightageDict = {}

	for i in range(n2):
		grade = input().lower()
		value = int(input())

		weightageDict[grade] = value


	pg = ProductGrade(dairyProducts,weightageDict)
	dairyBrand = input()
	productType = input()

	price = pg.priceBasedOnBrandAndType(dairyBrand,productType)

	if price:
		for item in price:
			print("Dairy Brand: ",item[0])
			print("Price: ",item[1])
	else:
		print("No dairy product found")