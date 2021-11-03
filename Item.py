# Question Link: https://tcsxplore2020.blogspot.com/2020/02/python-code-solution.html
# 25th January
# Q2

class Item:
	def __init__(self,*args):
		self.item_id = args[0]
		self.item_name = args[1]
		self.item_price = args[2]
		self.quantity_available = args[3]

	def calculate_price(self,itemQty):
		price = 0
		if itemQty >= self.quantity_available:
			price = itemQty*self.item_price
			return price
		else:
			return 0

class Store:
	def __init__(self,*args):
		self.item_list = args[0]

	def generate_bill(self,item):
		total_bill = 0

		for itemName, qnty in item.items():
			for item_obj in self.item_list:
				if item_obj.item_name==itemName:
					total_bill += item_obj.calculate_price(qnty)

		return total_bill

if __name__ == "__main__":
	noOfItems = int(input())
	itemList = []
	for i in range(noOfItems):
		item_id = int(input())
		item_name = input()
		item_price = int(input())
		quantity_available = int(input())

		I = Item(item_id,item_name,item_price,quantity_available)

		itemList.append(I)

	dictLen = int(input())
	itemDict = {}

	for j in range(dictLen):
		itemName = input()
		qty = int(input())

		itemDict[itemName] = qty

	print(itemList)
	print(itemList[0].calculate_price(2))
	S = Store(itemList)
	print(S.generate_bill(itemDict))