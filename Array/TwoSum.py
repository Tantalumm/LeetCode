class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        map = []
        result = []
        for i in range(len(nums)):
            x = target - nums[i] 
            if x in map :
                result.append(map.index(x)),result.append(i)
            else : map.append(nums[i])
        return result
             
        
sol = Solution 
print(sol.twoSum([1,2,3],3))

                



        