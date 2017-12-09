import re
line = [x.rstrip() for x in open('09.in','r').readlines()][0]
l = re.sub('!.','',line)
with_garbage = len(l)
l,count = re.subn('<.*?>','',l)
score = 1
total = 0
for c in l:
	if c == '{':
		score += 1
	elif c == '}':
		score -= 1
		total += score
print(total)
print(with_garbage - len(l) - 2*count)