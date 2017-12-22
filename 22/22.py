from collections import defaultdict

lines = open('22.in','r').read().rstrip().split('\n')
print(lines)
grid = defaultdict(int)
L = len(lines)//2
for Y,line in enumerate(lines):
	for X,c in enumerate(line):
		if c == '#':
			grid[(-L + X,L - Y)] = 1
pos = (0,0)
dels = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
i = 0
for _ in range(10000000):
	if grid[pos] == 1:
		d = (d+1) % 4
		grid[pos] = 2	# Flagged
	elif grid[pos] == 2:
		d = (d+2) % 4
		grid[pos] = 0	# Clean
	elif grid[pos] == 3:
		grid[pos] = 1	# Infected
		i += 1
	else:
		d = (d-1) % 4
		grid[pos] = 3	# Weakened
	pos = (pos[0]+dels[d][0],pos[1]+dels[d][1])
print(i)