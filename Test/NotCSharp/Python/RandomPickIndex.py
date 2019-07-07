# https://leetcode.com/problems/random-pick-index
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        for num in self.nums:
            if num == target:
                count +=1
        
        # now count holds the number of times we have seen that target number
        # the idea is that if we were to do random.randrange(count) - we will get a number between 0 and count
        # say count was 3, then we get a number from [0,1,2] with equal likelihood
        r = random.randrange(count)
        for idx, num in enumerate(self.nums):
            if num == target:
                if r == 0:
                    return idx
                else:
                    r -= 1        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)