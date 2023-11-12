#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

def sortColors(nums):
    n = len(nums)
    swapped = False
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swapped = True
                
        if swapped == False:
            break
        
nums = []
nums = [int(item) for item in input("enter input : ").split()]

Error01 = len(nums) > 300 or len(nums) < 1

def Error02(nums) :
    allowed_values = {0, 1, 2}
    result = set(nums) <= allowed_values
    return result

if Error01:
    print("Error because out of range")
else:    
    if Error02(nums) :
        sortColors(nums) 
        print(nums)
    else :
        print("Error because some value not allowed")
       

              








