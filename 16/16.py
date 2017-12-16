import re
lines = open('16.in','r').read().split(',')
#lines = ['s1','x3/4','pe/b']
order = [x for x in range(16)]
strs = []
for p in range(10000):
	for line in lines:
		if re.match('s',line):
			split = int(line[1:])
			order = order[(16-split):] + order[:(16-split)] 
		elif re.match('x',line):
			swap = [int(x) for x in line[1:].split('/')]
			a = order[swap[0]]
			order[swap[0]] = order[swap[1]]
			order[swap[1]] = a
		elif re.match('p',line):
			swap = [ord(x) - 97 for x in line[1:].split('/')]
			a = order.index(swap[0])
			b = order.index(swap[1])
			order[a] = swap[1]
			order[b] = swap[0]
	s = ''.join([chr(97 + x) for x in order])
	if s in strs:
		print(strs[1000000000 % p - 1])
		break
	else:
		strs.append(s)
		
print(''.join([chr(97 + x) for x in order]))