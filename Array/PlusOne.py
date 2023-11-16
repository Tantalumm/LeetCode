class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        result = int(''.join(map(str,digits)))
        result += 1
        result = [int(i) for i in str(result)]
        return result 

x = [1,2,3]
sol = Solution.plusOne(x)
print(sol)