line = [int(x) for x in open('06.in','r').read().split('\t')]
out = ','.join(map(str,line))
states = []
it = 0
while out not in states:
	states.append(out)
	it += 1
	maxnum = max(line)
	idx = line.index(maxnum)
	line[idx] = 0
	for _ in range(maxnum):
		idx += 1
		idx = idx % len(line)
		line[idx] += 1
	out = ','.join(map(str,line))
print(it)
print(it - states.index(out))