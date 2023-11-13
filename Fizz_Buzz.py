# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
class Solution(object):
    def fizzBuzz(n):
        fb_list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0 :
                fb_list.append("FizzBuzz")
            elif i % 3 == 0 :
                fb_list.append("Fizz")
            elif i % 5 == 0 :
                fb_list.append("Buzz")
            else:
                fb_list.append(str(i))
        return fb_list


n = int(input("n = "))
fizzBuzz = Solution.fizzBuzz(n)
print(fizzBuzz)       