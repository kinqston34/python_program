nums = [555,901,482,1771]
i = 0
even = 0
count = 0
while i < len(nums):
    if int(nums[i]) != 0:
        nums[i] = nums[i] / 10
        count += 1
    else:
        i += 1
        if count % 2 == 0:
            even += 1
            count = 0

print(even)