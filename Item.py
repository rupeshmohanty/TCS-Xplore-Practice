# Question Link: https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Q6
class Item:
	def __init__(self,*args):
		self.item_id = args[0]
		self.item_name = args[1]
		self.item_price = args[2]
		self.quantity_available = args[3]
	
	def calc_price(self,qty):
		if qty >= self.quantity_available:
			return self.price*qty
		else:
			return 0

class Store:
	def __init__(self,*args):
		self.item_list = args[0]
	
	def generate_bill(self,qtyDict):
		total_bill = 0
		for key in qtyDict.keys():
			for obj in self.item_list:
				if key.lower() == obj.item_name.lower():
					total_bill += obj.calc_price(qtyDict[key])
	
		return total_bill

if __name__ == "__main__":
	n = int(input())
	itemList = []

	for i in range(n):
		itemId = int(input())
		itemName = input()
		itemPrice = int(input())
		qtyAvailable = int(input())

		I = Item(itemId,itemName,itemPrice,qtyAvailable)
		itemList.append(I)
	
	qd = {}
	n1 = int(input())
	for j in range(n1):
		name = input()
		qty = int(input())
		qd[name] = qty
	
	S = Store(itemList)
	tot = S.generate_bill(qd)
	print(tot)

