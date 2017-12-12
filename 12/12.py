lines = [x.rstrip() for x in open('12.in','r').readlines()]
comms = []
for N,line in enumerate(lines):
	l = line.split()
	comms.append([int(x) for x in ''.join(l[2:]).split(',')])
groups = [x for x in range(0,2000)]
g = 0
while len(groups):
	parse = [groups[0]]
	result = [groups[0]]
	while len(parse):
		N = parse.pop(0)
		comm = comms[N]
		for c in comm:
			if c not in result:
				result.append(c)
				parse.append(c)
	for r in result:
		groups.remove(r)
	g += 1
	if result[0] == 0:
		print(len(result))
print(g)