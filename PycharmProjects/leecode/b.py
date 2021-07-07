#Given an array nums of integers, return how many of them contain an even number of digits.
# Input: nums = [12,345,2,6,7896]
# Output: 2
# 偶數位數的數字有幾個?
nums = [555,901,482,1771]
digit = []
count_even = 0
for i in nums:
    count = 1
    while (i//10) != 0:
        i = i//10
        count += 1
    if count % 2 == 0:
        count_even += 1
print(count_even)
