class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.outpput = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length = len(self.outpput)
        for i in range(length):
            j = random.randint(0, length - 1)
            self.outpput[i], self.outpput[j] = self.outpput[j], self.outpput[i]
        return self.outpput