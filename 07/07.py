import re

def weight(c):
	child_sum = []
	for child in children[c]:
		child_sum.append(weight(child))
	if len(list(set(child_sum))) > 1:
		badsum = min(child_sum,key=child_sum.count)
		badidx = child_sum.index(badsum)
		goodsum = max(child_sum,key=child_sum.count)
		print(weights[children[c][badidx]] - (badsum - goodsum))
	return weights[c] + sum(child_sum)

lines = [x.rstrip() for x in open('07.in','r').readlines()]
children = {}
weights = {}
for line in lines:
	arr = line.split()
	children[arr[0]] = []
	if len(arr) > 2:
		for a in arr[3:]:
			a = a.rstrip(',')
			children[arr[0]].append(a)
	weights[arr[0]] = int(re.match(r'\((\d+)\)',arr[1]).group(1))
all_my_children = [j for i in children.values() for j in i]
for node in children.keys():
	if node not in all_my_children:
		c = node
		break
print(c)
weight(c)