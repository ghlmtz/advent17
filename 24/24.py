X = 0
L = 0

def o(i,n):
	if ports[i][0] == n:
		return ports[i][1]
	else:
		return ports[i][0]

def search(q,i,c):
	global X,L
	#print('Searching for %d'%i)
	n = o(i,c)
	f = 0
	for N in range(len(ports)):
		if N in q:
			continue
		p = ports[N]
		if p[0] == n or p[1] == n:
			q.append(N)
			search(q,N,n)
			q.pop()
			f = 1
	if not f:
		s = sum([sum(ports[x]) for x in q])
		l = len(q)
		if l > L:
			L = l
			X = s
			print(l,s)
		elif l == L:
			if s > X:
				X = s
				print(l,s)
		#if s > X:
		#	print(s)
		#	X = s

lines = open('24.in','r').read().split('\n')
ports = []
zeroes = []
for N,line in enumerate(lines):
	t = [int(x) for x in line.split('/')]
	ports.append(t)
	if t[0] == 0 or t[1] == 0:
		zeroes.append(N)
for z in zeroes:
	q = [z]
	search(q,z,0)	
