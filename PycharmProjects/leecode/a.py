#find Max consecutiveOnes
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums = list(input('nums:'))
        count = 0
        current = []
        list1 = []
        for i in nums:
            list1.append(int(i))
        for i in list1:
            if i == 1:
                count += 1
            if i == 0:
                count = 0
            current.append(count)
        return max(current)
