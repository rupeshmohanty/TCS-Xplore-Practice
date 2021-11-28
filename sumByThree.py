n = int(input())
s = 0

while n > 0:
    s += n%10
    n = n // 10

if s % 3 == 0:
    print(True)
else:
    print(False)
