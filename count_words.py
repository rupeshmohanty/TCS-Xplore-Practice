# Question Link: https://themotivatingindian.in/tcs-opa-cpa-python-coding-questions-2021/
# Q.2.
def count_words(st):
	l = st.split(' ')
	wordCount = {}

	for i in l:
		if i in wordCount:
			wordCount[i] += 1
		else:
			wordCount[i] = 1

	return wordCount

def max_occurence_word(st):
	r = count_words(st)
	m = 0
	word = ""

	for i in list(r.keys()):
		if r[i] > m:
			m = r[i]
			word = i

	return word

if __name__ == "__main__":
	s = input()
	res = max_occurence_word(s)
	print(res)