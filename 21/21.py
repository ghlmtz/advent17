import re
lines = open('21.in','r').readlines()
rules2 = []
rules3 = []

def patt3(xy):
	x,y = xy
	#print(x,y)
	row = [patt[3*x+i][3*y:3*y+3] for i in range(3)]
	for _ in range(4):
		for r in rules3:
			if r[0][0] == row[0] and r[0][1] == row[1] and r[0][2] == row[2]:
				return r[1]
		row = [''.join(x) for x in list(zip(*row[::-1]))]
	row = row[::-1]
	for _ in range(4):
		for r in rules3:
			if r[0][0] == row[0] and r[0][1] == row[1] and r[0][2] == row[2]:
				return r[1]
		row = [''.join(x) for x in list(zip(*row[::-1]))]

def patt2(xy):
	x,y = xy
	row = [patt[2*x+i][2*y:2*y+2] for i in range(2)]
	#print(x,y,row)
	for _ in range(4):
		for r in rules2:
			if r[0][0] == row[0] and r[0][1] == row[1]:
				return r[1]
		row = [''.join(x) for x in list(zip(*row[::-1]))]
		#print(x,y,row)
	row = row[::-1]
	for _ in range(4):
		for r in rules2:
			if r[0][0] == row[0] and r[0][1] == row[1]:
				return r[1]
		row = [''.join(x) for x in list(zip(*row[::-1]))]


for line in lines:
	s = line.rstrip().split(' => ')
	rules3.append([(s[0].split('/')),(s[1].split('/'))])
for line in lines:
	s = line.rstrip().split(' => ')
	rules2.append([(s[0].split('/')),(s[1].split('/'))])
	#rules2.append((s[0].split('/'),s[1].split('/')),)
patt = ['#..#','....','....','#..#']

patt = ['.#.','..#','###']
for _ in range(18):
	npatt = []
	l = len(patt)
	if l % 2 == 0:	# Even
		for y in range(l//2):
			#for x in range(l//2):
			npatt.extend([''.join(a) for a in list(zip(*[patt2((y,x)) for x in range(l//2)]))])
	else:
		for y in range(l//3):
			npatt.extend([''.join(a) for a in list(zip(*[patt3((y,x)) for x in range(l//3)]))])
			#for x in range(l//3):
			#	npatt.append(patt3((x,y)))
	patt = npatt
	#print('\n'.join(patt))
	print(len(list(filter(lambda x: x == '#',''.join(patt)))))
#print(rules3)