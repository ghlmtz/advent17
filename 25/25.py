from collections import defaultdict
c = 0
x = 0
tape = defaultdict(int)
dirs = [(1,-1),(1,1),(-1,-1),(-1,1),(-1,1),(1,1)]
chg = [(1,3),(2,5),(2,0),(4,0),(0,1),(2,4)]
vals = [(1,0),(1,0),(1,1),(0,1),(1,0),(0,0)]
state = 0
halt = 12302209
while c < halt:
	i = tape[x]
	tape[x] = vals[state][i]
	x += dirs[state][i]
	state = chg[state][i]
	c += 1
	if c % 1000000 == 0:
		print(c)
print(len(tape))
print(sum(tape.values()))