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
		self.bList = args[2]
	
	def countOfBooks(self,s):
		c = 0
		for obj in self.bList:
			if obj.book_name[0].lower() == s.lower():
				c += 1
		
		return c

	def removeBooks(self,books):
		newList = []
		for obj in self.bList:
			if obj.book_name not in books:
				newList.append(obj.book_name)
		
		return newList

if __name__ == "__main__":
	n = int(input())
	bookList = []

	for i in range(n):
		book_id = int(input())
		book_name = input()
		B = Book(book_id,book_name)
		bookList.append(B)
	
	L = Library(1,"Bhubaneswar",bookList)
	s = input()
	count = L.countOfBooks(s)
	n1 = int(input())
	books = []

	for j in range(n1):
		bName = input()
		books.append(bName)
	
	res = L.removeBooks(books)

	print(count)
	
	for obj in res:
		print(obj)