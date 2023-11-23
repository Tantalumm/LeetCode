class Solution:
    def isPalindrome(x: str) -> bool:
        if x < 0 :
            return False
        tx = x
        rx = 0
        while tx != 0 :
            digit = tx % 10
            rx = rx * 10 + digit % 10
            tx //= 10
        return x == rx 


print(Solution.isPalindrome(121))