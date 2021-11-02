# Question Link: https://tcsxplore2020.blogspot.com/2020/02/python-code-solution.html
# 25th January
# Question 1
def check_prime(n):
	if n == 0 or n == 1:
		return -1
	else:
		for i in range(2,n):
			if n % i == 0:
				return 1
		return 0

def prime_composite_list(numberList):
	prime = []
	composite = []
	res = []

	for i in numberList:
		if check_prime(i) == 1:
			composite.append(i)
		elif check_prime(i) == 0:
			prime.append(i)
		else:
			pass

	res.append(prime)
	res.append(composite)

	return res

if __name__ == "__main__":
	numberList = list(map(int,input().split()))
	x = prime_composite_list(numberList)
	print(x)