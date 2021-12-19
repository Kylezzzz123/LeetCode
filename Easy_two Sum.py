# Given an array of integers, return indices of the the two numbers such that they add up to a specific target
# ex: Given nums = [2,7,11,15], target = 9
# nums[0] + nums[1] = 2+7 = target 9
# output: [0,1]


class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
             if target - nums[i] not in dict:    # target 9 - nums[i] 2 = 7 : reverse thinking --> 2+x= 9, 9 -2 =7, 2 and 7 can be in dict{}
                 dict[nums[i]] = i               # put the numbers into the dict[]
             else:
                return[dict[target-nums[i]],i]   # To determine there're no duplicate, and then show the list


