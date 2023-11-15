# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x
class Solution(object):
    def isPowerOfThree(n):
        if (n <= 0):
            return False
        if (n % 3 == 0):
            return Solution.isPowerOfThree(n//3)
        if (n == 1):
            return True
        return False
    

n = int(input("n = "))
input = Solution.isPowerOfThree(n)
    
print(input)       