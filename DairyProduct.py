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
		self.dList = args[0]
		self.wDict = args[1]
	
	def priceBasedOnBrandAndType(self,dBrand,pType):
		ans = []
		for obj in self.dList:
			if obj.dairyBrand.lower() == dBrand.lower() and obj.productType.lower() == pType.lower():
				obj.price = obj.price+obj.price*wDict[obj.grade]/100
				ans.append((dBrand,obj.price))
		
		if len(ans) > 0:
			return ans
		else:
			return None

if __name__ == "__main__":
	n = int(input())
	dairyList = []

	for i in range(n):
		dairyId = int(input())
		dairyBrand = input()
		productType = input()
		price = int(input())
		grade = input()

		D = DairyProduct(dairyId,dairyBrand,productType,price,grade)
		dairyList.append(D)
	
	n1 = int(input())
	wDict = dict()
	for j in range(n1):
		wGrade = input()
		weightage = int(input())
		wDict[wGrade] = weightage
	
	P = ProductGrade(dairyList,wDict)
	dBrand = input()
	pType = input()
	res = P.priceBasedOnBrandAndType(dBrand, pType)

	if len(res) > 0:
		for k in res:
			print(f'Dairy brand: {k[0]}')
			print(f'Price: {k[1]}')
	else:
		print("No dairy product found")