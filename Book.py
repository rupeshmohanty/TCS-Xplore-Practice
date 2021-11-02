class Book:
	def __init__(self,*args):
		self.book_id = args[0]
		self.book_name = args[1]

class Library:
	def __init__(self,*args):
		self.library_id = args[0]
		self.address = args[1]
		self.book_list = args[2]

	def books_count(self,c):
		count = 0
		for obj in self.book_list:
			if obj[0].lower() == c.lower():
				count += 1

		return count

	def delete_books(self,bList):
		for obj in bList:
			if obj in self.book_list:
				self.book_list.remove(obj)

		return self.book_list

n=int(input())
book_list=[]
for i in range(n):
    book_id=int(input())
    book_name=input()
    book_list.append(Book(book_id,book_name))
ch=input()
l=Library(123,"Mumbai",book_list)  
d_n=int(input())
list1=[]
for i in range(d_n):
    name=input()
    list1.append(name)

print(l.books_count(ch))
l.delete_books(list1)
for i in l.book_list:
    print(i.book_name)
