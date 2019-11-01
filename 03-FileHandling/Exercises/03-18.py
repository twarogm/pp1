nums = []
with open ('numbers.txt') as file:
    for line in file:
        nums.append(int(line))
nums = sorted(nums)
for i in nums:
    print(i, end = ' ')