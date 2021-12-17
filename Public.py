# https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
# Question 3
class PublicService:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.gender = args[2]
        self.distance = args[3]
    
def discount(passengerList,passId,discount):
    for obj in passengerList:
        if obj.id == passId:
            return discount*obj.distance / 100

if __name__ == "__main__":
    n = int(input())
    passengerList = []

    for i in range(n):
        pId = int(input())
        name = input()
        gender = input()
        distance = int(input())

        P = PublicService(pId,name,gender,distance)
        passengerList.append(P)
    
    passId = int(input())
    d = int(input())
    res = discount(passengerList, passId, d)

    print(f'discount of { passId } is : { res }')