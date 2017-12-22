import string
lines = [x.rstrip() for x in open('19.in','r').readlines()]
lines.append([' ' for x in range(200)])
s = set()
x = lines[0].index('|')
y = 0
d = 1
parttwo = 0
s = 0
while True:
	s += 1
	if parttwo:
		print(s)
	if d == 1:
		y += 1
	if d == 2:
		y -= 1
	if d == -1:
		x += 1
	if d == -2:
		x -= 1
	if lines[y][x] not in ['+','-','|']:
		print(lines[y][x])
	elif lines[y][x] == '+' and d > 0:
		if lines[y][x-1] == '-':
			d = -2
		elif lines[y][x+1] == '-':
			d = -1
		else:
			exit('DONE')
	elif lines[y][x] == '+' and d < 0:
		if len(lines[y+1]) >= x and lines[y+1][x] == '|':
			d = 1
		elif lines[y-1][x] == '|':
			d = 2
		else:
			exit('DONE')


