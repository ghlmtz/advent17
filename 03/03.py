from collections import defaultdict
n = 277678
i = 1
while i*i < n:
	i += 2
pivots = [i*i - k*(i-1) for k in range(5)]
for p in pivots:
	dist = abs(p - n)
	if dist <= (i-1)//2:
		print(i-1-dist)
		break

values = defaultdict(int)
values[(0,0)] = 1
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
d = -1
pos = (0,0)
while values[pos] <= n:
	d = (d+1)%4
	new_pos = tuple(map(sum,zip(pos,dirs[d])))
	if values[new_pos]:
		d = (d-1)%4
		new_pos = tuple(map(sum,zip(pos,dirs[d])))
	pos = new_pos
	x,y = pos
	s = 0
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			s += values[(i,j)]
	values[pos] = s
print(values[pos])