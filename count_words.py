# Question Link: https://themotivatingindian.in/tcs-opa-cpa-python-coding-questions-2021/
# Q.2.
def count_words(st):
	l = st.split()
	d = dict()

	for i in l:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	
	return d
	
def max_occurence_word(st):
	r = count_words(st)
	m = 0
	resStr = ""

	for i in list(r.keys()):
		if r[i] > m:
			m = r[i]
			resStr = i

	return resStr

if __name__ == "__main__":
	s = input()

	res = max_occurence_word(s)

	print(res)