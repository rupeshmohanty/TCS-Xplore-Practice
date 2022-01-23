# Question Link: https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-3/
class Dairyproduct:
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
		products = []
		for obj in self.dairyList:
			if obj.dairyBrand.lower() == dBrand.lower() and obj.productType.lower() == pType.lower():
				uprice = obj.price + obj.price*self.weightageDict[obj.grade]/100
				products.append((dBrand,uprice)) 
		
		if(len(products) > 0):
			return products
		else:
			return None

if __name__ == "__main__":
	dairyProducts = []
	n = int(input())

	for i in range(n):
		dairyId = int(input())
		dairyBrand = input()
		productType = input()
		price = int(input())
		grade = input()
		D = Dairyproduct(dairyId,dairyBrand,productType,price,grade)
		dairyProducts.append(D)
	
	n1 = int(input())
	wDict = dict()
	for j in range(n1):
		g = input()
		weightage = int(input())
		wDict[g] = weightage
	
	P = ProductGrade(dairyProducts,wDict)
	dBrand = input()
	pType = input()
	res = P.priceBasedOnBrandAndType(dBrand, pType)

	if res:
		for i in res:
			print(f"Dairy brand: { i[0] }")
			print(f"Dairy price: { i[1] }")
	else:
		print("No dairy products found!")