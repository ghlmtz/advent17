import re
import time
cmds = [x.split() for x in open('18.in','r').readlines()]
regs1 = [0 for _ in range(26)]
regs2 = [0 for _ in range(26)]
regs2[15] = 1
sound1 = []
sound2 = []
def getval1(r):
	if re.match('[\-0-9]',r):
		return int(r)
	else:
		return regs1[ord(r) - 97]
def getval2(r):
	if re.match('[\-0-9]',r):
		return int(r)
	else:
		return regs2[ord(r) - 97]
i1 = 0
i2 = 0
s = 0
wait1 = 0
wait2 = 0
p1 = set()
p2 = set()
while 0 <= i1 <= len(cmds) and 0 <= i2 <= len(cmds):
	cmd = cmds[i1]
	c = cmd[0]
	p1.add(i1)
	p2.add(i2)
	if c == 'jgz':
		if getval1(cmd[1]) > 0:
			i1 += getval1(cmd[2])
		else:
			i1 += 1
	else:
		if c == 'snd':
			sound2.append(getval1(cmd[1]))
		if c == 'set':
			regs1[ord(cmd[1]) - 97] = getval1(cmd[2])
		if c == 'add':
			regs1[ord(cmd[1]) - 97] += getval1(cmd[2])
		if c == 'mul':
			regs1[ord(cmd[1]) - 97] *= getval1(cmd[2])
		if c == 'mod':
			regs1[ord(cmd[1]) - 97] %= getval1(cmd[2])
		if c == 'rcv':
			if len(sound1):
				regs1[ord(cmd[1]) - 97] = sound1.pop(0)
				#print('1:',regs1[ord(cmd[1]) - 97])
				s += 1
			else:
				i1 -= 1
				wait1 = 1
				if wait2:
					print(s)
					exit()
		i1 += 1
	cmd = cmds[i2]
	c = cmd[0]
	if c == 'jgz':
		if getval2(cmd[1]) > 0:
			i2 += getval2(cmd[2])
		else:
			i2 += 1
	else:
		if c == 'snd':
			sound1.append(getval2(cmd[1]))
		if c == 'set':
			regs2[ord(cmd[1]) - 97] = getval2(cmd[2])
		if c == 'add':
			regs2[ord(cmd[1]) - 97] += getval2(cmd[2])
		if c == 'mul':
			regs2[ord(cmd[1]) - 97] *= getval2(cmd[2])
		if c == 'mod':
			regs2[ord(cmd[1]) - 97] %= getval2(cmd[2])
		if c == 'rcv':
			if len(sound2):
				regs2[ord(cmd[1]) - 97] = sound2.pop(0)
				#print('2:',regs2[ord(cmd[1]) - 97])
			else:
				i2 -= 1
				wait2 = 1
				if wait1:
					print(s)
					exit()
		i2 += 1