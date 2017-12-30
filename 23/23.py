import re
cmds = [x.split() for x in open('23.in','r').readlines()]
regs = [0 for _ in range(8)]
def getval(r):
	if re.match('[\-0-9]',r):
		return int(r)
	else:
		return regs[ord(r) - 97]
i1 = 0
m = 0
while 0 <= i1 < len(cmds):
	cmd = cmds[i1]
	c = cmd[0]
	if c == 'jnz':
		if getval(cmd[1]) != 0:
			i1 += getval(cmd[2])
		else:
			i1 += 1
	else:
		if c == 'set':
			regs[ord(cmd[1]) - 97] = getval(cmd[2])
		if c == 'sub':
			regs[ord(cmd[1]) - 97] -= getval(cmd[2])
		if c == 'mul':
			regs[ord(cmd[1]) - 97] *= getval(cmd[2])
			m += 1
		i1 += 1
print(m)
h = 0
for x in range(105700,122700 + 1,17):
	for i in range(2,x):
		if x % i == 0:
			h += 1
			break
print(h)