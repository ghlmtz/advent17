lines = open('20.in','r').readlines()
p = []
v = []
a = []
collide = [0 for x in range(len(lines))]
for line in lines:
	pva = line.split()
	p.append([int(x) for x in pva[0][3:-2].split(',')])
	v.append([int(x) for x in pva[1][3:-2].split(',')])
	a.append([int(x) for x in pva[2][3:-1].split(',')])
print(v)
for _ in range(1000):
	s = []
	for N in range(len(lines)):
		v[N] = [v[N][0] + a[N][0],v[N][1] + a[N][1],v[N][2] + a[N][2]]
		p[N] = [v[N][0] + p[N][0],v[N][1] + p[N][1],v[N][2] + p[N][2]]
		s.append(sum(map(abs,map(int,p[N]))))
	c = []
	for N in range(len(lines)):
		if collide[N]:
			continue
		for M in range(N):
			if collide[M]:
				continue
			if p[N][0] == p[M][0] and p[N][1] == p[M][1] and p[N][2] == p[M][2]:
				c.append(N)
				c.append(M)
	for b in c:
		collide[b] = 1
	print(s.index(min(s)))
	print('Ans:',len(lines) - sum(collide))