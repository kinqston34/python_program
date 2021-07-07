nums = [3,3]
target = 9
dic ={}
for i in range(len(nums)):
    if target - nums[i] not in dic:
        dic[nums[i]] = i
    else:
        n = target - nums[i]
        print(dic[n],i)