i = 'wenycdww'
from functools import reduce
hashes = []
s = 0
array = []
for n in range(128):
	our_str = "%s-%d" % (i,n)
	lens = [ord(x) for x in our_str]
	lens.extend([17,31,73,47,23])
	nums = [x for x in range(0,256)]
	pos = 0
	skip = 0
	for _ in range(64):
		for l in lens:
			to_reverse = []
			for x in range(l):
				n = (pos + x) % 256
				to_reverse.append(nums[n])
			to_reverse.reverse()
			for x in range(l):
				n = (pos + x) % 256
				nums[n] = to_reverse[x]
			pos += l + skip
			pos = pos % 256
			skip += 1
	dense = []
	for x in range(0,16):
		subslice = nums[16*x:16*x+16]
		dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
	hex_str = ''.join(dense)

	new_row = []
	for c in hex_str:
		N = int(c,16)
		new_row.extend(list("{0:04b}".format(N)))
		s += "{0:b}".format(N).count('1')
	array.append(new_row)
print(s)
ff = [[0 for x in range(128)] for y in range(128)]
regions = []
def _floodFill(xy,group,stack):
	x,y = xy
	if ff[x][y]:
		return
	if array[x][y] == '0':
		return
	ff[x][y] = True
	group.append((x,y))
	if x > 0 and not ff[x-1][y]:
		stack.append((x-1,y))
	if x < 127 and not ff[x+1][y]:
		stack.append((x+1,y))
	if y > 0 and not ff[x][y-1]:
		stack.append((x,y-1))
	if y < 127 and not ff[x][y+1]:
		stack.append((x,y+1))

def floodFill():
	stack = []
	for x in range(128):
		for y in range(128):
			r = array[x][y]

			if ff[x][y]:
				continue

			if array[x][y] == '1':

				stack.append((x,y))
				arr = []

				while(len(stack) > 0):
					_floodFill(stack.pop(),arr,stack)

				if(len(arr)):
					regions.append(arr)
			else:
				ff[x][y] = True
floodFill()
print(len(regions))