from numpy import random
class Solution(object):

    def __init__(self, nums):
        self.main = nums 
        self.backup = nums[:] 
        self.length = len(self.main)

    def reset(self):
        return self.backup
        

    def shuffle(self):
        n = self.length - 1
        i = 0
        while(i <= n+1):
            pos1 = random.randint(0,n)
            pos2 = random.randint(0,n)
            self.main[pos1],self.main[pos2] = self.main[pos2],self.main[pos1]
            i += 1
        return self.main
        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
print(obj.reset())
print(obj.shuffle())
# param_1 = obj.reset()
# param_2 = obj.shuffle()