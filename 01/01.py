### Part one ###
with open('01.in','r') as f:
	line = f.read().rstrip()
s = 0 if line[0] != line[-1] else int(line[0])
for N, x in enumerate(line[:-2]):
	if x == line[N+1]:
		s += int(x)
print(s)
### Part two ###
antipode = len(line)//2
s = 0
for N, x in enumerate(line[:-2]):
	if x == line[(N + antipode)%len(line)]:
		s += int(x)
print(s)