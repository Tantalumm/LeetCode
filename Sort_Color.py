#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.
class Solution(object):
    def sortColors(colors):
        n = len(colors)
        swapped = False
        for i in range(n):
            for j in range(0,n-i-1):
                if colors[j] > colors[j+1]:
                    colors[j],colors[j+1] = colors[j+1],colors[j]
                    swapped = True
                
            if swapped == False:
                break
    def Error01():
        return len(input) > 300 or len(input) < 1

    def Error02(colors) :
        allowed_values = {0, 1, 2}
        result = set(colors) <= allowed_values
        return result


input = input()
input = input.replace('[','').replace(']','')
input = [int(item) for item in input.split(",")]

if Solution.Error01():
    if Solution.Error02(input) :
        Solution.sortColors(input) 
        print(input)
    else :
        print("Error because some value not allowed")
else:    
    print("Error because out of range")

       

              








