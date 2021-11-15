# Question Link: https://themotivatingindian.in/tcs-opa-cpa-python-coding-questions-2021/
# Q.1.
def check_palindrome(l):
	res = []

	for i in l:
		if i == i[::-1]:
			res.append(i)

	return res

if __name__ == "__main__":
	list_of_strings = list(map(str,input().split()))
	r = check_palindrome(list_of_strings)

	for i in r:
		print(i)