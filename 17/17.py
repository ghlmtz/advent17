spin = 366
pos = 0
arr = [0]
for x in range(1,2018):
	pos += spin
	pos = pos % len(arr)
	arr.insert(pos+1,x)
	pos = arr.index(x)
print(arr[arr.index(2017)+1])

l = 1
p = 0
n = 0
for x in range(1,50000001):
	p += spin
	p = 1 + p % l
	l += 1
	if p == 1:
		n = x
print(n)
