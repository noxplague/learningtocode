m = int(raw_input())
n = int(raw_input())

if m < n:
	t = m
	m = n
	n = t

r = m % n

while r > 0:
	m = n
	n = r
	r = m % n

if r == 0:
	print n



