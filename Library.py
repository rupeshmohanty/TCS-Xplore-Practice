# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 7
class Book:
    def __init__(self,*args):
        self.book_id = args[0]
        self.book_name = args[1]
    
class Library:
    def __init__(self,*args):
        self.library_id = args[0]
        self.address = args[1]
        self.bookList = args[2]
    
    def countOfBooks(self,ch):
        count = 0

        for obj in self.bookList:
            if obj.book_name[0].lower() == ch.lower():
                count += 1
        
        return count
    
    def removeBooks(self,rList):
        for n in rList:
            for obj in self.bookList:
                if obj.book_name.lower() == n.lower():
                    self.bookList.remove(obj)

if __name__ == "__main__":
    n = int(input())
    bList = []

    for i in range(n):
        bId = int(input())
        bName = input()

        B = Book(bId,bName)
        bList.append(B)

    L = Library(1,"Bhubaneswar",bList)
    ch = input()

    n1 = int(input())
    rList = []
    for j in range(n1):
        bn = input()
        rList.append(bn)
    
    c = L.countOfBooks(ch)

    print(c)
    L.removeBooks(rList)
    for k in bList:
        print(k.book_name)
