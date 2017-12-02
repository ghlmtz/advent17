### Part one ###
s = 0
with open('02.in','r') as f:
	for line in f:
		nums = [int(c) for c in line.split('\t')]
		s += max(nums) - min(nums)
print(s)
### Part two ###
s = 0
with open('02.in','r') as f:
	for line in f:
		nums = [int(c) for c in line.split('\t')]
		for N, num in enumerate(nums):
			for other_num in nums[N+1:]:
				if num % other_num == 0:
					s += num//other_num
					break
				elif other_num % num == 0:
					s += other_num//num
					break
print(s)