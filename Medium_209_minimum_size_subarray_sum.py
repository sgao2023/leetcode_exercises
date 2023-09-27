class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
#The basic idea is "sliding window". 
        left=0
        right=0
        total=nums[0]
        min_length=len(nums)
        flag=-1
        while left<=right and right<len(nums):
            if total<target:
                if right+1<=len(nums)-1: 
#The index right+1 might be out of range. Need to take care of it. 
                    right+=1
                    total=total+nums[right]
                else:
                    break
            else:
                min_length=min(right-left+1,min_length)
                flag=1
"""
Pay attention to the order of the following two sentences. In my first try, I swithched their order
which result in substraction of wrong number. 
"""
                total=total-nums[left]
                left+=1
                
        if flag==-1: 
#flag==-1 means the scenario "total>=target" has never happened.
            return 0
        else:
            return min_length