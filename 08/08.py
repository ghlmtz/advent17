from collections import defaultdict
def oper(test,op,val):
	if op == '<':
		return regs[test] < val
	elif op == '==':
		return regs[test] == val
	elif op == '>':
		return regs[test] > val
	elif op == '>=':
		return regs[test] >= val
	elif op == '<=':
		return regs[test] <= val
	elif op == '!=':
		return not(regs[test]==val)

lines = [x.rstrip() for x in open('08.in','r').readlines()]
regs = defaultdict(int)
maxval = 0
for line in lines:
	cmd = line.split()
	test = cmd[4]
	op = cmd[5]
	val = int(cmd[6])
	if oper(test,op,val):
		amount = int(cmd[2])
		if cmd[1] == 'dec':
			regs[cmd[0]] = regs[cmd[0]] - amount
		else:
			regs[cmd[0]] = regs[cmd[0]] + amount
	if max(regs.values()) > maxval:
		maxval = max(regs.values())
print(max(regs.values()))
print(maxval)