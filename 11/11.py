dirs = open('11.in','r').read().split(',')
axis = [0,0,0]
maxdist = 0
for d in dirs:
	if d == 'sw':
		axis[2] += 1
		axis[0] -= 1
	if d == 's':
		axis[2] += 1
		axis[1] -= 1
	if d == 'n':
		axis[1] += 1
		axis[2] -= 1
	if d == 'ne':
		axis[0] += 1
		axis[2] -= 1
	if d == 'nw':
		axis[1] += 1
		axis[0] -= 1
	if d == 'se':
		axis[0] += 1
		axis[1] -= 1
	m = max(map(abs, axis))
	if m > maxdist:
		maxdist = m
print(m)
print(maxdist)