# Question Link: https://tcsxplore2020.blogspot.com/2020/02/python-code-solution.html
# Question 2
class Book:
	def __init__(self,*args):
		self.book_id = args[0]
		self.book_name = args[1]
	
class Library:
	def __init__(self,*args):
		self.library_id = args[0]
		self.address = args[1]
		self.book_list = args[2]
	
	def books_count(self,s):
		count = 0

		for obj in self.book_list:
			if obj.book_name[0].lower() == s.lower():
				count += 1
		
		return count
	
	def delete_books(self,bList):
		for obj1 in bList:
			for obj2 in self.book_list:
				if obj1.lower() == obj2.book_name.lower():
					self.book_list.remove(obj2)
		
if __name__ == "__main__":
	n = int(input())
	book_list = list()

	for i in range(n):
		book_id = int(input())
		book_name = input()

		B = Book(book_id,book_name)
		book_list.append(B)
	
	ch = input()

	n1 = int(input())
	bList = list()
	for j in range(n1):
		bookName = input()

		bList.append(bookName)

	L = Library(123,"Bhubaneswar",book_list)
	c = L.books_count(ch)
	L.delete_books(bList)

	print(c)
	
	for r in book_list:
		print(r.book_name) 