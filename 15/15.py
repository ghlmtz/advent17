### For part 1, remove while loops in genA() and genB()
### and change the for loop to 40 million

def genA(seed1):
	seed1 *= 16807
	seed1 = seed1 % 2147483647
	while(seed1 % 4):
		seed1 *= 16807
		seed1 = seed1 % 2147483647
	return seed1 

def genB(seed2):
	seed2 *= 48271
	seed2 = seed2 % 2147483647
	while(seed2 % 8):
		seed2 *= 48271
		seed2 = seed2 % 2147483647
	return seed2

def bitgen(seed1,seed2):
	while True:
		seed1 = genA(seed1)
		seed2 = genB(seed2)
		mseed1 = seed1 & 0xFFFF
		mseed2 = seed2 & 0xFFFF
		yield mseed1 ^ mseed2
#g = bitgen(65,8921)
g = bitgen(783,325)
print(sum([not next(g) for x in range(5000000)]))